def create_deviation_index_dict():
    #min -4, max 8
    index_dict = {
        'soft 20,3': '8,D',
        'soft 20,4': '6,D',
        'soft 20,5': '5,D',
        'soft 20,6': '4,D',
        'soft 19,2': '8,D',
        'soft 19,3': '5,D',
        'soft 19,4': '3,D',
        'soft 19,5': '1,D',
        'soft 19,6': '1,D',
        'soft 18,2': '1,D', #quand cound above (normalement 0)
        'soft 18,3': '-2,-',
        'soft 18,A': '1,-',
        'soft 17,2': '1,D',
        'soft 17,3': '-3,H',
        'soft 16,3': '4,D',
        'soft 16,4': '-2,H',
        'soft 15,3': '7,D',
        'soft 15,4': '-1,H', #quand count below (normalement 0)
        'soft 15,5': '-4,H',
        'soft 14,3': '7,D',
        'soft 14,4': '1,D',
        'soft 14,5': '-1,H',
        'soft 14,6': '-4,H',
        'soft 13,3': '7,D',
        'soft 13,4': '3,D',
        'soft 13,5': '-1,H', #quand count below
        'soft 13,6': '-1,H',
        'hard 16,8': '7,-',
        'hard 16,9': '5,-',
        'hard 16,T': '1,-', # normalement 0
        'hard 16,A': '8,-',
        'hard 15,9': '8,-',
        'hard 15,T': '4,-',
        'hard 14,2': '-3,H',
        'hard 14,3': '-4,H',
        'hard 13,2': '-4,H',
        'hard 13,3': '-1,H', # normaement 0
        'hard 13,4': '-1,H',
        'hard 13,5': '-3,H',
        'hard 13,6': '-4,H',
        'hard 12,2': '3,-',
        'hard 12,3': '2,-',
        'hard 12,4': '-1,H', #normalement 0
        'hard 12,5': '-1,H', #comprends pas la
        'hard 12,6': '-1,H', # normalement 0
        'hard 11,9': '-4,H',
        'hard 11,T': '4,D',
        'hard 10,8': '-4,H',
        'hard 10,9': '-1,H',
        'hard 9,2': '1,D',
        'hard 9,3': '-1,H', #quand count est below normelemtn 0
        'hard 9,4': '-2,H',
        'hard 9,5': '-4,D',
        'hard 9,7': '3,D',
        'hard 9,8': '7,D',
        'hard 8,4': '5,D',
        'hard 8,5': '3,D',
        'hard 8,6': '1,D',
        'pair T,3': '8,S',
        'pair T,4': '6,S',
        'pair T,5': '5,S',
        'pair T,6': '4,S',
        'pair 9,2': '-2,-',
        'pair 9,3': '-3,-',
        'pair 9,7': '3,S',
        'pair 7,8': '5,S',
        'pair 6,2': '-1,H',
        'pair 6,3': '-4,H',
        'pair 5,8': '-4,H',
        'pair 5,9': '-1,H',
        'pair 4,3': '8,S',
        'pair 4,4': '3,S', # needs to be checked
        'pair 4,5': '-1,S',
        'pair 4,6': '-2,S',
        'pair 3,2': '-1,H', # quand count below normalement 0
        'pair 3,3': '-4,H',
        'pair 3,8': '4,S',
        'pair 2,2': '-3,H',
        'pair 2,8': '5,S',
    }
    # print(index_dict)
    return index_dict

def high_low_count(card):
    if card in ['A','T']:
        return -1
    if card in ['7', '8', '9']:
        return 0
    return 1

def high_low_hand(hand):
    count = 0
    for card in hand:
        count += high_low_count(card)
    return count

def calc_true_count(count, deck):
    return int(round(52*float(count)/sum(deck.values()), 0))