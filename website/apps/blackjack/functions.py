CARD_VALUE = {
    'A': 11,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}
def order_hand(hand):
    card_list = [*hand]
    card_list = sorted(card_list, key=CARD_VALUE.get, reverse=True)
    return ''.join(card_list)