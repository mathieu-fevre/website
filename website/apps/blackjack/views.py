from django.shortcuts import render, redirect

from website.apps.blackjack.basic_strategy import DECK_VALUE, create_basic_strategy, create_basic_strategy_no_double, create_basic_strategy_no_double_no_split, create_basic_strategy_no_split


def display_basic_strategy(request):
    basic_strategy = create_basic_strategy()
    dec_list = []
    for total in range(21, 4, -1):
        dec_list.append('hard '+str(total))
        for card in DECK_VALUE:
            key = 'hard '+ str(total)+','+card
            dec_list.append(basic_strategy[key])
    for total in range(21, 12, -1):
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
            
    # basic_strategy_no_split = create_basic_strategy_no_split()
    # dec_list_no_split = []
    # for total in range(21, 4, -1):
    #     dec_list_no_split.append('hard '+str(total))
    #     for card in DECK_VALUE:
    #         key = 'hard '+ str(total)+','+card
    #         dec_list_no_split.append(basic_strategy_no_split[key])
    # for total in range(21, 12, -1):
    #     if total == 21:
    #         dec_list_no_split.append('AT')
    #     else:
    #         dec_list_no_split.append('A'+str(total-11))
    #     for card in DECK_VALUE:
    #         key = 'soft '+ str(total)+','+card
    #         dec_list_no_split.append(basic_strategy_no_split[key])
    # for card in reversed(DECK_VALUE):
    #     dec_list_no_split.append(card+card)
    #     for bank_card in DECK_VALUE: 
    #         key = 'pair ' + card + ',' + bank_card
    #         dec_list_no_split.append(basic_strategy_no_split[key])
            
    # basic_strategy_no_double_no_split = create_basic_strategy_no_double_no_split()
    # dec_list_no_double_no_split = []
    # for total in range(21, 4, -1):
    #     dec_list_no_double_no_split.append('hard '+str(total))
    #     for card in DECK_VALUE:
    #         key = 'hard '+ str(total)+','+card
    #         dec_list_no_double_no_split.append(basic_strategy_no_double_no_split[key])
    # for total in range(21, 12, -1):
    #     if total == 21:
    #         dec_list_no_double_no_split.append('AT')
    #     else:
    #         dec_list_no_double_no_split.append('A'+str(total-11))
    #     for card in DECK_VALUE:
    #         key = 'soft '+ str(total)+','+card
    #         dec_list_no_double_no_split.append(basic_strategy_no_double_no_split[key])
    # for card in reversed(DECK_VALUE):
    #     dec_list_no_double_no_split.append(card+card)
    #     for bank_card in DECK_VALUE: 
    #         key = 'pair ' + card + ',' + bank_card
    #         dec_list_no_double_no_split.append(basic_strategy_no_double_no_split[key])
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
        # 'dec_list_no_double': dec_list_no_double,
        # 'dec_list_no_split': dec_list_no_split,
        # 'dec_list_no_double_no_split': dec_list_no_double_no_split,
    }
    return render(request, 'blackjack/display_basic_strategy.html', contexts)
