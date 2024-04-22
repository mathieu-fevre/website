from django.shortcuts import render, redirect

from website.apps.blackjack.basic_strategy import DECK_VALUE, create_basic_strategy


def display_basic_strategy(request):
    basic_strategy = create_basic_strategy()
    dec_list = []
    for total in range(21, 4, -1):
        dec_list.append('hard '+str(total))
        for card in DECK_VALUE:
            key = 'hard '+ str(total)+','+card
            dec_list.append(basic_strategy[key])
    for total in range(21, 13, -1):
        if total == 21:
            dec_list.append('AT')
        else:
            dec_list.append('A'+str(total-11))
        for card in DECK_VALUE:
            key = 'soft '+ str(total)+','+card
            dec_list.append(basic_strategy[key])
    for card in reversed(DECK_VALUE):
        dec_list.append(card+card)
        for bank_card in DECK_VALUE: 
            key = 'pair ' + card + ',' + bank_card
            dec_list.append(basic_strategy[key])
    color_dict = {
        '-': 'red',
        'H': '#83f28f',
        'S': 'pink',
        'D': '#FCE205',
    }
    contexts = {
        'dec_list': dec_list,
        'deck_value': DECK_VALUE,
        'color_dict': color_dict,
    }
    return render(request, 'blackjack/display_basic_strategy.html', contexts)
