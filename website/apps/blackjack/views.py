from django.forms import modelformset_factory
from django.shortcuts import render, redirect

from website.apps.blackjack.basic_strategy import DECK_VALUE, create_basic_strategy, create_basic_strategy_no_double, create_basic_strategy_no_double_no_split, create_basic_strategy_no_split
from website.apps.blackjack.card_counter import create_deviation_index_dict
from website.apps.blackjack.forms import ComparisonDecisionAddForm, ComparisonDecisionForm, HandDecisionEVForm
from website.apps.blackjack.models import ComparisonDecision, HandDecisionEV, ProbBankResults
from django.contrib import messages
from multiprocessing import Process
from django import db
from django.db.models import F

from website.apps.blackjack.utils import create_new_comparison, create_new_hand_decision_ev, number_of_hands_per_shoe, player_plays_particular_hand, player_plays_with_bet, player_plays_with_bet_and_count, value_hand

def display_basic_strategy(request):
    color_dict = {
        '-': 'red',
        'H': '#83f28f',
        'S': 'pink',
        'D': '#FCE205',
    }
    index_list = create_deviation_index_dict()
    counts_list = []
    basic_strategy = create_basic_strategy()
    dec_list = []
    for total in range(21, 4, -1):
        dec_list.append('hard '+str(total))
        counts_list.append(['hard '+str(total), '#A9A9A9'])
        for card in DECK_VALUE:
            key = 'hard '+ str(total)+','+card
            dec_list.append(basic_strategy[key])
            if key in index_list:
                count = index_list[key].split(',')[0]
                color = color_dict[index_list[key].split(',')[1]]
                counts_list.append([count, color])
            else:
                counts_list.append(['', '#FFFFFF'])
    for total in range(21, 12, -1):
        if total == 21:
            dec_list.append('AT')
            counts_list.append(['AT', '#A9A9A9'])
        else:
            dec_list.append('A'+str(total-11))
            counts_list.append(['A'+str(total-11), '#A9A9A9'])
        for card in DECK_VALUE:
            key = 'soft '+ str(total)+','+card
            dec_list.append(basic_strategy[key])
            if key in index_list:
                count = index_list[key].split(',')[0]
                color = color_dict[index_list[key].split(',')[1]]
                counts_list.append([count, color])
            else:
                counts_list.append(['', '#FFFFFF'])
    for card in reversed(DECK_VALUE):
        dec_list.append(card+card)
        counts_list.append([card+card, '#A9A9A9'])
        for bank_card in DECK_VALUE: 
            key = 'pair ' + card + ',' + bank_card
            dec_list.append(basic_strategy[key])
            if key in index_list:
                count = index_list[key].split(',')[0]
                color = color_dict[index_list[key].split(',')[1]]
                counts_list.append([count, color])
            else:
                counts_list.append(['', '#FFFFFF'])
            
    basic_strategy_no_double = create_basic_strategy_no_double()
    dec_list_no_double = []
    for total in range(21, 4, -1):
        dec_list_no_double.append('hard '+str(total))
        for card in DECK_VALUE:
            key = 'hard '+ str(total)+','+card
            dec_list_no_double.append(basic_strategy_no_double[key])
    for total in range(21, 12, -1):
        if total == 21:
            dec_list_no_double.append('AT')
        else:
            dec_list_no_double.append('A'+str(total-11))
        for card in DECK_VALUE:
            key = 'soft '+ str(total)+','+card
            dec_list_no_double.append(basic_strategy_no_double[key])
    for card in reversed(DECK_VALUE):
        dec_list_no_double.append(card+card)
        for bank_card in DECK_VALUE: 
            key = 'pair ' + card + ',' + bank_card
            dec_list_no_double.append(basic_strategy_no_double[key])
            
    basic_strategy_no_split = create_basic_strategy_no_split()
    dec_list_no_split = []
    for total in range(21, 4, -1):
        dec_list_no_split.append('hard '+str(total))
        for card in DECK_VALUE:
            key = 'hard '+ str(total)+','+card
            dec_list_no_split.append(basic_strategy_no_split[key])
    for total in range(21, 12, -1):
        if total == 21:
            dec_list_no_split.append('AT')
        else:
            dec_list_no_split.append('A'+str(total-11))
        for card in DECK_VALUE:
            key = 'soft '+ str(total)+','+card
            dec_list_no_split.append(basic_strategy_no_split[key])
    for card in reversed(DECK_VALUE):
        dec_list_no_split.append(card+card)
        for bank_card in DECK_VALUE: 
            key = 'pair ' + card + ',' + bank_card
            dec_list_no_split.append(basic_strategy_no_split[key])
            
    basic_strategy_no_double_no_split = create_basic_strategy_no_double_no_split()
    dec_list_no_double_no_split = []
    for total in range(21, 4, -1):
        dec_list_no_double_no_split.append('hard '+str(total))
        for card in DECK_VALUE:
            key = 'hard '+ str(total)+','+card
            dec_list_no_double_no_split.append(basic_strategy_no_double_no_split[key])
    for total in range(21, 12, -1):
        if total == 21:
            dec_list_no_double_no_split.append('AT')
        else:
            dec_list_no_double_no_split.append('A'+str(total-11))
        for card in DECK_VALUE:
            key = 'soft '+ str(total)+','+card
            dec_list_no_double_no_split.append(basic_strategy_no_double_no_split[key])
    for card in reversed(DECK_VALUE):
        dec_list_no_double_no_split.append(card+card)
        for bank_card in DECK_VALUE: 
            key = 'pair ' + card + ',' + bank_card
            dec_list_no_double_no_split.append(basic_strategy_no_double_no_split[key])
    contexts = {
        'counts_list': counts_list,
        'dec_list': dec_list,
        'deck_value': DECK_VALUE,
        'color_dict': color_dict,
        'dec_list_no_double': dec_list_no_double,
        'dec_list_no_split': dec_list_no_split,
        'dec_list_no_double_no_split': dec_list_no_double_no_split,
    }
    return render(request, 'blackjack/display_basic_strategy.html', contexts)

def display_hand_decision_ev(request):
    keys_stand = []
    keys_hit = []
    keys_double = []
    keys_split = []
    for total in range(21, 4, -1):
        keys_stand.append('hard '+str(total))
        keys_hit.append('hard '+str(total))
        keys_double.append('hard '+str(total))
    for total in range(21, 12, -1):
        keys_stand.append('soft '+ str(total))
        keys_hit.append('soft '+ str(total))
        keys_double.append('soft '+ str(total))
    for card in reversed(DECK_VALUE):
        keys_stand.append('pair '+ card)
        keys_hit.append('pair '+ card)
        keys_double.append('pair '+ card)
        keys_split.append('pair '+ card)
    form = HandDecisionEVForm()
    if request.POST:
        if 'compute' in request.POST:
            form = HandDecisionEVForm(request.POST)
            if form.is_valid():
                db.connections.close_all()
                hand = form.cleaned_data['hand']
                bank_card = form.cleaned_data['bank_card']
                decision = form.cleaned_data['decision']
                number_of_decks = 6
                number_of_simulations = form.cleaned_data['number_of_simulations']
                obj = HandDecisionEV.objects.filter(hand=hand, decision=decision, bank_card=bank_card, number_of_decks=number_of_decks, number_of_simulations__gte=number_of_simulations)
                if obj.exists():
                    messages.add_message(request, messages.ERROR, 'This simulation already exists with of number of simulations of ' + str(obj.first().number_of_simulations) +'.')
                else:
                    # p = Process(target=create_new_hand_decision_ev, args=(hand, bank_card, decision, number_of_decks, number_of_simulations))
                    # p.start()
                    # messages.add_message(request, messages.SUCCESS, 'Simulations started')
                    messages.add_message(request, messages.SUCCESS, 'service In construction')
                    return redirect(request.get_full_path())
            else:
                messages.add_message(request, messages.ERROR, 'Error in the form')
    contexts = {
        'form': form,
        'keys_stand': keys_stand,
        'keys_hit': keys_hit,
        'keys_split': keys_split,
        'keys_double': keys_double,
        'deck_value': DECK_VALUE,
    }
    return render(request, 'blackjack/display_hand_decision_ev.html', contexts)

def compare_results(request):
    comp_dec = ComparisonDecision.objects.all()
    form = ComparisonDecisionAddForm()
    if request.POST:
        if 'add' in request.POST:
            form = ComparisonDecisionAddForm(request.POST)
            if form.is_valid():
                db.connections.close_all()
                hand = form.cleaned_data['hand']
                bank_card = form.cleaned_data['bank_card']
                decision1 = form.cleaned_data['decision1']
                decision2 = form.cleaned_data['decision2']
                number_of_decks = form.cleaned_data['number_of_decks']
                number_of_simulations = form.cleaned_data['number_of_simulations']
                p = Process(target=create_new_comparison, args=(hand, bank_card, decision1, decision2, number_of_decks, number_of_simulations))
                p.start()
                messages.add_message(request, messages.SUCCESS, 'Simulations started')
                return redirect(request.get_full_path())
            else:
                messages.add_message(request, messages.ERROR, 'Error in the form')
    contexts = {
        'comp_dec': comp_dec,
        'form': form,
    }
    return render(request, 'blackjack/compare_results.html', contexts)

def compare_add(request):
    Formset = modelformset_factory(ComparisonDecision, form=ComparisonDecisionForm, extra=1, can_delete=True)
    formset = Formset(queryset=ComparisonDecision.objects.all())
    if request.POST:
        if 'save' in request.POST:
            formset = Formset(request.POST)
            if formset.is_valid():
                formset.save()
                messages.add_message(request, messages.SUCCESS, 'Comparison added !')
                return redirect(request.get_full_path())
            else:
                messages.add_message(request, messages.ERROR, 'Comparison failed !')
    contexts = {
        'formset': formset
    }
    return render(request, 'blackjack/compare_add.html', contexts)
    
def display_bank_results(request):
    overall_results = ProbBankResults.objects.filter(bank_card__isnull=True).first()
    objs = sorted(ProbBankResults.objects.filter(bank_card__isnull=False), key=lambda x:value_hand(x.bank_card))
    contexts = {
        'objs': objs,
        'overall_results': overall_results
    }
    return render(request, 'blackjack/display_bank_results.html', contexts)