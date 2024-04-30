import random
from math import floor
from website.apps.blackjack.basic_strategy import create_basic_strategy, DECK_VALUE, create_basic_strategy_no_double, create_basic_strategy_no_double_no_split, create_basic_strategy_no_split
import time
from copy import deepcopy
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np
from django import db
from multiprocessing import Process
import django
django.setup()

from website.apps.blackjack.card_counter import high_low_count, true_count
from website.apps.blackjack.models import ComparisonDecision, HandDecisionEV

basic_strategy = create_basic_strategy()
basic_strategy_no_double = create_basic_strategy_no_double()
basic_strategy_no_split = create_basic_strategy_no_split()
basic_strategy_no_double_no_split = create_basic_strategy_no_double_no_split()
number_of_decks = 6
initial_deck = {'2': 4*number_of_decks, '3': 4*number_of_decks, '4': 4*number_of_decks, '5': 4*number_of_decks, '6': 4*number_of_decks, '7': 4*number_of_decks, '8': 4*number_of_decks, '9': 4*number_of_decks, 'T': 16*number_of_decks, 'A': 4*number_of_decks}
initial_deck2 = {'2': 4*number_of_decks, '3': 4*number_of_decks, '4': 4*number_of_decks, '5': 4*number_of_decks, '6': 4*number_of_decks, '7': 4*number_of_decks, '8': 4*number_of_decks, '9': 4*number_of_decks, 'T': 16*number_of_decks, 'A': 4*number_of_decks}
cut_decks = 4.5

def reset_all():
    global basic_strategy, basic_strategy_no_double, basic_strategy_no_split, basic_strategy_no_double_no_split, number_of_decks, initial_deck, initial_deck2, cut_decks
    basic_strategy = create_basic_strategy()
    basic_strategy_no_double = create_basic_strategy_no_double()
    basic_strategy_no_split = create_basic_strategy_no_split()
    basic_strategy_no_double_no_split = create_basic_strategy_no_double_no_split()
    number_of_decks = 6
    initial_deck = {'2': 4*number_of_decks, '3': 4*number_of_decks, '4': 4*number_of_decks, '5': 4*number_of_decks, '6': 4*number_of_decks, '7': 4*number_of_decks, '8': 4*number_of_decks, '9': 4*number_of_decks, 'T': 16*number_of_decks, 'A': 4*number_of_decks}
    initial_deck2 = {'2': 4*number_of_decks, '3': 4*number_of_decks, '4': 4*number_of_decks, '5': 4*number_of_decks, '6': 4*number_of_decks, '7': 4*number_of_decks, '8': 4*number_of_decks, '9': 4*number_of_decks, 'T': 16*number_of_decks, 'A': 4*number_of_decks}
    cut_decks = 4.5
    
def draw_card(deck):
    total = sum(deck.values())
    number = floor(total*random.random()+1)
    for card in deck.keys():
        if number <= deck[card]:
            deck[card] -= 1
            return card, deck
        number -= deck[card]
        
def draw_card_no_deck(deck):
    total = sum(deck.values())
    number = floor(total*random.random()+1)
    for card in deck.keys():
        if number <= deck[card]:
            return card
        number -= deck[card]

def value_hand(hand):
    total = 0
    for card in hand:
        if card == 'T':
            total += 10
        elif card == 'A':
            total += 11
        else:
            total += int(card)
    if total >21 and 'A' in hand:
        new_total = total-10*(hand.count('A')-1)
        if new_total <22:
            return new_total
        return new_total-10
    return total

def bank_score(hand, deck):
    value = value_hand(hand)
    while value < 17:
        card, deck = draw_card(deck)
        hand += card
        value = value_hand(hand)
    return hand, deck

def bank_score_value_no_deck(hand, deck):
    value = value_hand(hand)
    while value < 17:
        card = draw_card_no_deck(deck)
        hand += card
        value = value_hand(hand)
    return value

def who_wins(player_hand, bank_hand):
    player_hand_value = value_hand(player_hand)
    if player_hand_value > 21:
        return -1
    bank_hand_value = value_hand(bank_hand)
    if bank_hand_value > 21:
        return 1
    if player_hand_value > bank_hand_value:
        return 1
    if player_hand_value < bank_hand_value:
        return -1
    if player_hand_value != 21 or (len(player_hand)>2 and len(bank_hand)>2) or (len(player_hand)==2 and len(bank_hand)==2):
        return 0
    if len(player_hand)>2 and len(bank_hand)==2:
        return -1
    return 1

def hand_to_key(hand):
    value = value_hand(hand)
    if value>21:
        return 'bust'
    if hand == 'AA':
        return 'pair A'
    if 'A' in hand:
        if value_hand(hand+'T')<22:
            return 'soft ' + str(value)
        return 'hard ' + str(value)
    if len(hand)==2:
        if hand[0]==hand[1]:
            return 'pair ' + hand[0]
    return 'hard ' + str(value)

def player_single_action(hand1, hand2, hand3, bank_hand, deck):
    player_key = hand_to_key(hand1)
    if player_key == 'bust':
        return hand1, hand2, hand3, deck, '-', 1
    if hand3 and hand2:
        if len(hand1)>=3:
            decision = basic_strategy_no_double_no_split[player_key + ',' + bank_hand]
        else:
            decision = basic_strategy_no_split[player_key + ',' + bank_hand]
    else:
        if len(hand1)>=3:
            decision = basic_strategy_no_double[player_key + ',' + bank_hand]
        else:
            decision = basic_strategy[player_key + ',' + bank_hand]
    if decision == '-':
        return hand1, hand2, hand3, deck, decision, 1
    if decision == 'D':
        card, deck = draw_card(deck)
        hand1 += card
        return hand1, hand2, hand3, deck, decision, 2 
    if decision == 'H':
        card, deck = draw_card(deck)
        hand1 += card
        return hand1, hand2, hand3, deck, decision, 1
    if decision == 'S':
        hand1 = hand1[0]
        card, deck = draw_card(deck)
        hand1 += card
        if hand2 == '':
            hand2 = hand1[0]
            card, deck = draw_card(deck)
            hand2 += card
            return hand1, hand2, hand3, deck, decision, 1
        else:
            hand1 = hand1[0]
            card, deck = draw_card(deck)
            hand1 += card
            hand3 = hand1[0]
            card, deck = draw_card(deck)
            hand3 += card
            return hand1, hand2, hand3, deck, decision, 1

# les mains sont pas forcément dans l'ordre de départ
def player_actions(hand1, hand2, hand3, bank_hand, deck, decision=None, bet1=None, bet2=None, bet3=None):
    # print('1: '+hand1, '2: '+hand2, '3: '+hand3, 'bank: '+bank_hand, deck, decision, bet1, bet2, bet3)
    if decision == '-' or decision == 'D':
        if bet1:
            return hand1, hand2, hand3, deck, bet1, bet2, bet3
    hand1, hand2, hand3, deck, decision, bet1 = player_single_action(hand1, hand2, hand3, bank_hand, deck)
    if not hand2 or bet2 or decision == 'S' or decision == 'H':
        if hand2 and hand1[0]=='A' and hand2[0]=='A':
            return hand1, hand2, hand3, deck, 1, 1, bet3 # Quand on split des As, une carte par as, pas de blackjack et pas de 3ieme jeu.
        return player_actions(hand1, hand2, hand3, bank_hand, deck, decision, bet1, bet2, bet3)
    return player_actions(hand2, hand3, hand1, bank_hand, deck, decision, bet2, bet3, bet1)
    
def player_plays_one_hand(hand, bank_hand, deck):
    return player_actions(hand, '', '', bank_hand, deck)

def initialize_hand(deck):
    if sum(deck.values()) <= float(sum(initial_deck.values()))*(1-cut_decks/number_of_decks):
        deck = {'2': 4*number_of_decks, '3': 4*number_of_decks, '4': 4*number_of_decks, '5': 4*number_of_decks, '6': 4*number_of_decks, '7': 4*number_of_decks, '8': 4*number_of_decks, '9': 4*number_of_decks, 'T': 16*number_of_decks, 'A': 4*number_of_decks}
    hand, deck = draw_card(deck)
    bank_hand, deck = draw_card(deck)
    card, deck= draw_card(deck)
    hand += card
    return hand, bank_hand, deck

def get_gain_from_one_hand(deck):
    gain_total = 0
    hand, bank_hand, deck = initialize_hand(deck)
    if hand == 'AT' or hand == 'TA':
        bank_hand, deck = bank_score(bank_hand, deck)
        if bank_hand != 'AT' and bank_hand != 'TA':      ##                             
            gain_total +=  3/2
    else:                                               ##
        hand1, hand2, hand3, deck, bet1, bet2, bet3 = player_plays_one_hand(hand, bank_hand, deck)
        bank_hand, deck = bank_score(bank_hand, deck)
        if bank_hand == 'AT' or bank_hand == 'TA':
            gain_total -= bet1
            if hand2:
                gain_total -= bet2
            if hand3:
                gain_total -= bet3
        else:
            gain_total += bet1 * who_wins(hand1, bank_hand)
            if hand2:
                gain_total += bet2 * who_wins(hand2, bank_hand)
            if hand3:
                gain_total += bet3 * who_wins(hand3, bank_hand)
    return gain_total, deck

def player_plays(hands_number, deck):
    gain = 0
    for _ in range(1, hands_number+1):
        gain_total, deck = get_gain_from_one_hand(deck)
        gain += gain_total
    return gain

def calc_ev(hands_number, deck):
    return 100 * float(player_plays(hands_number, deck))/hands_number

def player_plays_one_hand_with_bet(bet, deck):
    gain = 0
    hand, bank_hand, deck = initialize_hand(deck)
    if hand == 'AT' or hand == 'TA':
        bank_hand, deck = bank_score(bank_hand, deck)
        if bank_hand != 'AT' and bank_hand != 'TA':      ##                             
            gain +=  3/2 *bet
    else:                                               ##
        hand1, hand2, hand3, deck, bet1, bet2, bet3 = player_plays_one_hand(hand, bank_hand, deck)
        bank_hand, deck = bank_score(bank_hand, deck)
        if bank_hand == 'AT' or bank_hand == 'TA':
            gain -= bet1 * bet
            if hand2:
                gain -= bet2 * bet
            if hand3:
                gain -= bet3 *bet
        else:    
            gain += bet1 * who_wins(hand1, bank_hand) *bet
            if hand2:
                gain += bet2 * who_wins(hand2, bank_hand) *bet
            if hand3:
                gain += bet3 * who_wins(hand3, bank_hand) *bet
    return gain, deck

def player_plays2(hands_number, deck, bet):
    gain = 0
    for _ in range(1, hands_number+1):
        gain += player_plays_one_hand_with_bet(bet, deck)
    return gain

def calc_ev2(hands_number, deck):
    return 100 * float(player_plays2(hands_number, deck, 1))/hands_number

def get_trajectory_list(bankroll, hands_number, deck):
    bankroll_list = [bankroll]
    current_br = bankroll
    for i in range(1, hands_number+1):
        gain_total, deck = get_gain_from_one_hand(deck)
        current_br += gain_total
        bankroll_list.append(current_br)
        if current_br <=0:
            return bankroll_list, i
    return bankroll_list, hands_number

def trace_trajectory(bankroll, hands_number, deck):
    bankroll_list, i = get_trajectory_list(bankroll, hands_number, deck)
    plt.plot(range(1, len(bankroll_list)+1), bankroll_list)
    plt.title("Bankroll evolution")
    plt.xlabel("Hand number")
    plt.ylabel("Bankroll")
    plt.grid()
    plt.show() 

def get_percentage_ruin(bankroll, hands_number, deck, number_of_simulations):
    number_of_ruin = 0
    for _ in range(1, number_of_simulations+1):
        current_br = bankroll
        for i in range(1, hands_number+1):
            gain_total, deck = get_gain_from_one_hand(deck)
            current_br += gain_total
            if current_br <=0:
                number_of_ruin +=1
                break
    return 100 * float(number_of_ruin)/number_of_simulations

def get_percentage_with_max(bankroll, goal, hands_number, deck, number_of_simulations):
    number_of_ruin = 0
    number_of_success = 0
    for _ in range(1, number_of_simulations+1):
        current_br = bankroll
        for i in range(1, hands_number+1):
            gain_total, deck = get_gain_from_one_hand(deck)
            current_br += gain_total
            if current_br <=0:
                number_of_ruin +=1
                break
            elif current_br >= goal:
                number_of_success +=1
                break
    ruin_percentage = 100 * float(number_of_ruin)/number_of_simulations
    sucess_percentage = 100 * float(number_of_success)/number_of_simulations
    return sucess_percentage, ruin_percentage

def get_br_result_percentage_with_max(bankroll, goal, hands_number, deck, number_of_simulations):
    result = {'0': 0, str(goal): 0}
    for _ in range(1, number_of_simulations+1):
        current_br = bankroll
        for i in range(1, hands_number+1):
            gain_total, deck = get_gain_from_one_hand(deck)
            current_br += gain_total
        if current_br <=0:
            result['0'] +=1
        elif current_br >= goal:
            result[str(goal)] +=1
        elif str(current_br) in result:
            result[str(current_br)] +=1
        else:
            result[str(current_br)] =1
    percentage_dict = {}
    for key in result.keys():
        percentage_dict[key] = 100 * float(result[key])/number_of_simulations
    result_list = [float(key)-bankroll for key, val in result.items() for _ in range(val)]
    # plt.bar(percentage_dict.keys(), percentage_dict.values(), color='g')
    plt.hist(result_list, weights=np.ones(len(result_list)) / number_of_simulations, bins=50, range=[min(result_list)-1, max(result_list)+1])
    plt.grid()
    plt.gca().yaxis.set_major_formatter(PercentFormatter(1))
    plt.show()
    return percentage_dict

def get_trajectory_list_with_bet(bankroll, bet, hands_number, deck):
    bankroll_list = [bankroll]
    current_br = bankroll
    for i in range(1, hands_number+1):
        gain_total, deck = player_plays_one_hand_with_bet(bet, deck)
        current_br += gain_total
        bankroll_list.append(current_br)
        if current_br <=0:
            return bankroll_list, i
    return bankroll_list, hands_number

def trace_trajectory_with_bet(bankroll, bet, hands_number, deck):
    bankroll_list, i = get_trajectory_list_with_bet(bankroll, bet, hands_number, deck)
    plt.plot(range(1, len(bankroll_list)+1), bankroll_list)
    plt.title("Bankroll evolution with bet: "+str(bet))
    plt.xlabel("Hand number")
    plt.ylabel("Bankroll")
    plt.grid()
    plt.show() 

def get_percentage_ruin_with_bet(bankroll, bet, hands_number, deck, number_of_simulations):
    number_of_ruin = 0
    for _ in range(1, number_of_simulations+1):
        current_br = bankroll
        for i in range(1, hands_number+1):
            gain_total, deck = player_plays_one_hand_with_bet(bet, deck)
            current_br += gain_total
            if current_br <=0:
                number_of_ruin +=1
                break
    return 100 * float(number_of_ruin)/(number_of_simulations)

def get_percentage_with_max_with_bet(bankroll, bet, goal, hands_number, deck, number_of_simulations):
    number_of_ruin = 0
    number_of_success = 0
    for _ in range(1, number_of_simulations+1):
        current_br = bankroll
        for i in range(1, hands_number+1):
            gain_total, deck = player_plays_one_hand_with_bet(bet, deck)
            current_br += gain_total
            if current_br <=0:
                number_of_ruin +=1
                break
            elif current_br >= goal:
                number_of_success +=1
                break
    ruin_percentage = 100 * float(number_of_ruin)/number_of_simulations
    sucess_percentage = 100 * float(number_of_success)/number_of_simulations
    return sucess_percentage, ruin_percentage

def count_frequency(deck, min_count, max_count, number_of_simulations):
    count = 0
    count_dict = {} 
    for i in range (min_count, max_count+1):
        count_dict[str(i)] = 0
    for _ in range (1, number_of_simulations+1):
        if sum(deck.values()) <= float(sum(initial_deck.values()))*(1-cut_decks/number_of_decks):
            count = 0
            deck = {'2': 4*number_of_decks, '3': 4*number_of_decks, '4': 4*number_of_decks, '5': 4*number_of_decks, '6': 4*number_of_decks, '7': 4*number_of_decks, '8': 4*number_of_decks, '9': 4*number_of_decks, 'T': 16*number_of_decks, 'A': 4*number_of_decks}
        card1, deck = draw_card(deck)
        bank_hand, deck = draw_card(deck)
        card2, deck = draw_card(deck)
        card3, deck = draw_card(deck)
        count += high_low_count(bank_hand) + high_low_count(card1) + high_low_count(card2) + high_low_count(card3)
        true_count_var = true_count(count, deck)
        if true_count_var >= max_count:
            count_dict[str(max_count)] += 1
        elif true_count_var <= min_count:
            count_dict[str(min_count)] += 1
        else:
            count_dict[str(true_count_var)] += 1
    percentage_dict = {}
    for key in count_dict.keys():
        percentage_dict[key] = 100 * float(count_dict[key])/number_of_simulations
    # count_list = [key for key, val in count_dict.items() for _ in range(val)]
    # plt.hist(count_list, bins=max_count-min_count+1)
    plt.bar(percentage_dict.keys(), percentage_dict.values(), color='g')
    plt.grid()
    plt.show()
    return percentage_dict

def player_plays_particular_hand(hand, bank_hand, hands_number, deck):
    gain = 0
    for _ in range(1, hands_number+1):
        deck = {'2': 4*number_of_decks, '3': 4*number_of_decks, '4': 4*number_of_decks, '5': 4*number_of_decks, '6': 4*number_of_decks, '7': 4*number_of_decks, '8': 4*number_of_decks, '9': 4*number_of_decks, 'T': 16*number_of_decks, 'A': 4*number_of_decks}
        for card in hand:
            deck[card] = deck[card]-1
        deck[bank_hand] = deck[bank_hand]-1
        if hand == 'AT' or hand == 'TA':
            bank_hand2, deck = bank_score(bank_hand, deck)
            if bank_hand2 != 'AT' and bank_hand2 != 'TA':      ##                             
                gain +=  3/2
        else:                                               ##
            hand1, hand2, hand3, deck, bet1, bet2, bet3 = player_plays_one_hand(hand, bank_hand, deck)
            bank_hand2, deck = bank_score(bank_hand, deck)
            if bank_hand2 == 'AT' or bank_hand2 == 'TA':
                gain -= bet1
                if hand2:
                    gain -= bet2
                if hand3:
                    gain -= bet3
            else:
                gain += bet1 * who_wins(hand1, bank_hand2)
                if hand2:
                    gain += bet2 * who_wins(hand2, bank_hand2)
                if hand3:
                    gain += bet3 * who_wins(hand3, bank_hand2)
    # print('hand1: '+hand1, 'hand2: '+hand2, 'hand3: '+ hand3, 'bank_hand:' + bank_hand2, 'bet1: '+str(bet1), 'bet2: '+str(bet2), 'bet3: '+str(bet3), 'gain: '+ str(gain))
    return gain

def calc_ev_particular_hand(hand, bank_hand, hands_number, deck):
    return 100 * float(player_plays_particular_hand(hand, bank_hand, hands_number, deck))/hands_number

def calc_ev_particular_hand_decision_changed(hand, bank_hand, hands_number, deck, decision=None):
    if decision:
        key = hand_to_key(hand)+','+bank_hand
        global basic_strategy, basic_strategy_no_double, basic_strategy_no_split, basic_strategy_no_double_no_split
        basic_strategy[key] = decision
        if decision != 'D':
            basic_strategy_no_double[key] = decision
        if decision != 'S':
            basic_strategy_no_split[key] = decision
        if decision != 'S' and decision != 'D':
            basic_strategy_no_double_no_split[key] = decision
    ev = calc_ev_particular_hand(hand, bank_hand, hands_number, deck)
    reset_all()
    return ev

def compare(hand, bank_hand, decision1, decision2, hands_number, deck):
    ev1 = calc_ev_particular_hand_decision_changed(hand, bank_hand, hands_number, deck, decision1)
    ev2 = calc_ev_particular_hand_decision_changed(hand, bank_hand, hands_number, deck, decision2)
    return ev1, ev2

def prob_result_bank(number_of_simulations, deck, card=None):
    result_dict = {
        17: 0, 
        18: 0,
        19: 0,
        20: 0,
        21: 0,
        'bust': 0,
        }
    for _ in range(1, number_of_simulations+1):
        if not card:
            card = draw_card_no_deck(deck)
        value = bank_score_value_no_deck(card, deck)
        if value > 21:
            result_dict['bust'] += 1
        else:
            result_dict[value] +=1
    percentage_dict = {
        
    }
    for key in result_dict.keys():
        percentage_dict[key] = 100 * float(result_dict[key]) /number_of_simulations
    return percentage_dict

def create_new_comparison(hand, bank_card, decision1, decision2, number_of_decks, number_of_simulations):
    deck = {'2': 4*number_of_decks, '3': 4*number_of_decks, '4': 4*number_of_decks, '5': 4*number_of_decks, '6': 4*number_of_decks, '7': 4*number_of_decks, '8': 4*number_of_decks, '9': 4*number_of_decks, 'T': 16*number_of_decks, 'A': 4*number_of_decks}
    ev1, ev2 = compare(hand, bank_card, decision1, decision2, number_of_simulations, deck)
    key = hand_to_key(hand) +','+bank_card
    theoritical_decision = basic_strategy[key]
    if ev1>ev2:
        exp_decision = decision1
    else:
        exp_decision = decision2
    ComparisonDecision.objects.create(hand=hand, bank_card=bank_card, decision1=decision1, decision2=decision2, ev1=ev1, ev2=ev2,
                                        theoritical_decision=theoritical_decision, exp_decision=exp_decision,
                                        number_of_decks=number_of_decks, number_of_simulations=number_of_simulations)
    db.connections.close_all()
    
def create_new_hand_decision_ev(hand, bank_card, decision, number_of_decks, number_of_simulations):
    deck = {'2': 4*number_of_decks, '3': 4*number_of_decks, '4': 4*number_of_decks, '5': 4*number_of_decks, '6': 4*number_of_decks, '7': 4*number_of_decks, '8': 4*number_of_decks, '9': 4*number_of_decks, 'T': 16*number_of_decks, 'A': 4*number_of_decks}
    ev = calc_ev_particular_hand_decision_changed(hand, bank_card, number_of_simulations, deck, decision=None)
    key = hand_to_key(hand)
    obj = HandDecisionEV.objects.filter(hand=hand, bank_card=bank_card, decision=decision, number_of_decks=number_of_decks, key=key).first()
    if obj:
        obj.ev = ev
        obj.number_of_simulations = number_of_simulations
        obj.save()
    else:
        HandDecisionEV.objects.create(hand=hand, bank_card=bank_card, decision=decision, number_of_decks=number_of_decks, key=key, number_of_simulations=number_of_simulations, ev=ev)
    db.connections.close_all()

def launch():
    create_new_hand_decision_ev('65', '5', 'D', 6, 1000)
    number_of_simulations = 10000000
    number_of_decks = 6
    decision = '-'
    hands_list = ['342', '62', '43', '42', '32', '83']
    for hand in hands_list:
        for card in DECK_VALUE:
            create_new_hand_decision_ev(hand, card, decision, number_of_decks, number_of_simulations)