DECK_VALUE = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'A']

def create_basic_strategy():
    basic_strategy = {}
    for i in range(17,22):
        for j in  DECK_VALUE:
            basic_strategy['hard ' + str(i) + ',' + j] = '-'
    for i in range(12,17):
        for j in  ['2', '3', '4', '5', '6']:
            basic_strategy['hard ' + str(i) + ',' + j] = '-'
        for j in  ['7', '8', '9', 'T', 'A']:
            basic_strategy['hard ' + str(i) + ',' + j] = 'H'
    basic_strategy['hard 12,2'] = 'H'
    basic_strategy['hard 12,3'] = 'H'
    for i in range(9,12):
        for j in  ['2', '3', '4', '5', '6', '7', '8', '9']:
            basic_strategy['hard ' + str(i) + ',' + j] = 'D'
    basic_strategy['hard 11,T'] = 'H'
    basic_strategy['hard 11,A'] = 'H'
    basic_strategy['hard 10,T'] = 'H'
    basic_strategy['hard 10,A'] = 'H'
    for i in range(5,10):
        for j in  DECK_VALUE:
            basic_strategy['hard ' + str(i) + ',' + j] = 'H'
    basic_strategy['hard 9,3'] = 'D'
    basic_strategy['hard 9,4'] = 'D'
    basic_strategy['hard 9,5'] = 'D'
    basic_strategy['hard 9,6'] = 'D'
    for j in ['2', '3', '4', '5', '6', '7', '8', '9', 'T']:
        basic_strategy['pair A,' + j] = 'S'
    basic_strategy['pair A,A'] = 'H'
    for j in DECK_VALUE:
        basic_strategy['pair T,' + j] = '-'
    for j in ['2', '3', '4', '5', '6', '8', '9']:
        basic_strategy['pair 9,' + j] = 'S'
    basic_strategy['pair 9,' + '7'] = '-'
    basic_strategy['pair 9,' + 'T'] = '-'
    basic_strategy['pair 9,' + 'A'] = '-'
    for j in ['2', '3', '4', '5', '6', '7', '8', '9']:
        basic_strategy['pair 8,' + j] = 'S'
    basic_strategy['pair 8,' + 'T'] = 'H'
    basic_strategy['pair 8,' + 'A'] = 'H'
    for j in ['2', '3', '4', '5', '6', '7']:
        basic_strategy['pair 7,' + j] = 'S'
    basic_strategy['pair 7,' + 'T'] = 'H'
    basic_strategy['pair 7,' + 'A'] = 'H'
    basic_strategy['pair 7,' + '8'] = 'H'
    basic_strategy['pair 7,' + '9'] = 'H'
    for j in ['2', '3', '4', '5', '6']:
        basic_strategy['pair 6,' + j] = 'S'
    basic_strategy['pair 6,' + 'T'] = 'H'
    basic_strategy['pair 6,' + 'A'] = 'H'
    basic_strategy['pair 6,' + '8'] = 'H'
    basic_strategy['pair 6,' + '9'] = 'H'
    basic_strategy['pair 6,' + '7'] = 'H'
    for j in ['2', '3', '4', '5', '6', '7', '8', '9']:
        basic_strategy['pair 5,' + j] = 'D'
    basic_strategy['pair 5,' + 'T'] = 'H'
    basic_strategy['pair 5,' + 'A'] = 'H'
    for j in DECK_VALUE:
        basic_strategy['pair 4,' + j] = 'H'
    basic_strategy['pair 4,' + '5'] = 'S'
    basic_strategy['pair 4,' + '6'] = 'S'
    for i in range(2, 4):
        for j in ['2', '3', '4', '5', '6', '7']:
            basic_strategy['pair ' + str(i) + ',' + j] = 'S'
        for j in ['8', '9', 'T', 'A']:
            basic_strategy['pair ' + str(i) + ',' + j] = 'H'
    for j in DECK_VALUE:
        basic_strategy['soft 21,' + j] = '-'
        basic_strategy['soft 20,' + j] = '-'
        basic_strategy['soft 19,' + j] = '-'
    for i in range(2, 8):
        for j in DECK_VALUE:
            basic_strategy['soft ' + str(11+i) + ',' + j] = 'H'
    basic_strategy['soft 18,2'] = '-'
    basic_strategy['soft 18,7'] = '-'
    basic_strategy['soft 18,8'] = '-'
    basic_strategy['soft 18,5'] = 'D'
    basic_strategy['soft 18,6'] = 'D'
    basic_strategy['soft 18,4'] = 'D'
    basic_strategy['soft 18,3'] = 'D'
    basic_strategy['soft 17,6'] = 'D'
    basic_strategy['soft 17,5'] = 'D'
    basic_strategy['soft 17,4'] = 'D'
    basic_strategy['soft 17,3'] = 'D'
    basic_strategy['soft 16,6'] = 'D'
    basic_strategy['soft 16,5'] = 'D'
    basic_strategy['soft 16,4'] = 'D'
    basic_strategy['soft 15,6'] = 'D'
    basic_strategy['soft 15,5'] = 'D'
    basic_strategy['soft 15,4'] = 'D'
    basic_strategy['soft 14,6'] = 'D'
    basic_strategy['soft 14,5'] = 'D'
    basic_strategy['soft 13,6'] = 'D'
    basic_strategy['soft 13,5'] = 'D'
    # print(basic_strategy)
    return basic_strategy

def create_basic_strategy_no_split():
    basic_strategy = {}
    for i in range(17,22):
        for j in  DECK_VALUE:
            basic_strategy['hard ' + str(i) + ',' + j] = '-'
    for i in range(12,17):
        for j in  ['2', '3', '4', '5', '6']:
            basic_strategy['hard ' + str(i) + ',' + j] = '-'
        for j in  ['7', '8', '9', 'T', 'A']:
            basic_strategy['hard ' + str(i) + ',' + j] = 'H'
    basic_strategy['hard 12,2'] = 'H'
    basic_strategy['hard 12,3'] = 'H'
    for i in range(9,12):
        for j in  ['2', '3', '4', '5', '6', '7', '8', '9']:
            basic_strategy['hard ' + str(i) + ',' + j] = 'D'
    basic_strategy['hard 11,T'] = 'H'
    basic_strategy['hard 11,A'] = 'H'
    basic_strategy['hard 10,T'] = 'H'
    basic_strategy['hard 10,A'] = 'H'
    for i in range(5,10):
        for j in  DECK_VALUE:
            basic_strategy['hard ' + str(i) + ',' + j] = 'H'
    basic_strategy['hard 9,3'] = 'D'
    basic_strategy['hard 9,4'] = 'D'
    basic_strategy['hard 9,5'] = 'D'
    basic_strategy['hard 9,6'] = 'D'
    for j in ['2', '3', '4', '5', '6', '7', '8', '9', 'T']:
        basic_strategy['pair A,' + j] = 'H'
    basic_strategy['pair A,A'] = 'H'
    for j in DECK_VALUE:
        basic_strategy['pair T,' + j] = '-'
    for j in ['2', '3', '4', '5', '6', '8', '9']:
        basic_strategy['pair 9,' + j] = '-'
    basic_strategy['pair 9,' + '7'] = '-'
    basic_strategy['pair 9,' + 'T'] = '-'
    basic_strategy['pair 9,' + 'A'] = '-'
    for j in ['2', '3', '4', '5', '6']:
        basic_strategy['pair 8,' + j] = '-'
    basic_strategy['pair 8,' + '7'] = 'H'
    basic_strategy['pair 8,' + '8'] = 'H'
    basic_strategy['pair 8,' + '9'] = 'H'
    basic_strategy['pair 8,' + 'T'] = 'H'
    basic_strategy['pair 8,' + 'A'] = 'H'
    for j in ['2', '3', '4', '5', '6']:
        basic_strategy['pair 7,' + j] = '-'
    basic_strategy['pair 7,' + 'T'] = 'H'
    basic_strategy['pair 7,' + 'A'] = 'H'
    basic_strategy['pair 7,' + '8'] = 'H'
    basic_strategy['pair 7,' + '9'] = 'H'
    basic_strategy['pair 7,' + '7'] = 'H'
    for j in ['4', '5', '6']:
        basic_strategy['pair 6,' + j] = '-'
    basic_strategy['pair 6,' + 'T'] = 'H'
    basic_strategy['pair 6,' + 'A'] = 'H'
    basic_strategy['pair 6,' + '8'] = 'H'
    basic_strategy['pair 6,' + '9'] = 'H'
    basic_strategy['pair 6,' + '7'] = 'H'
    basic_strategy['pair 6,' + '2'] = 'H'
    basic_strategy['pair 6,' + '3'] = 'H'
    for j in ['2', '3', '4', '5', '6', '7', '8', '9']:
        basic_strategy['pair 5,' + j] = 'D'
    basic_strategy['pair 5,' + 'T'] = 'H'
    basic_strategy['pair 5,' + 'A'] = 'H'
    for j in DECK_VALUE:
        basic_strategy['pair 4,' + j] = 'H'
    for i in range(2, 4):
        for j in DECK_VALUE:
            basic_strategy['pair ' + str(i) + ',' + j] = 'H'
    for j in DECK_VALUE:
        basic_strategy['soft 21,' + j] = '-'
        basic_strategy['soft 20,' + j] = '-'
        basic_strategy['soft 19,' + j] = '-'
    for i in range(2, 8):
        for j in DECK_VALUE:
            basic_strategy['soft ' + str(11+i) + ',' + j] = 'H'
    basic_strategy['soft 18,2'] = '-'
    basic_strategy['soft 18,7'] = '-'
    basic_strategy['soft 18,8'] = '-'
    basic_strategy['soft 18,5'] = 'D'
    basic_strategy['soft 18,6'] = 'D'
    basic_strategy['soft 18,4'] = 'D'
    basic_strategy['soft 18,3'] = 'D'
    basic_strategy['soft 17,6'] = 'D'
    basic_strategy['soft 17,5'] = 'D'
    basic_strategy['soft 17,4'] = 'D'
    basic_strategy['soft 17,3'] = 'D'
    basic_strategy['soft 16,6'] = 'D'
    basic_strategy['soft 16,5'] = 'D'
    basic_strategy['soft 16,4'] = 'D'
    basic_strategy['soft 15,6'] = 'D'
    basic_strategy['soft 15,5'] = 'D'
    basic_strategy['soft 15,4'] = 'D'
    basic_strategy['soft 14,6'] = 'D'
    basic_strategy['soft 14,5'] = 'D'
    basic_strategy['soft 13,6'] = 'D'
    basic_strategy['soft 13,5'] = 'D'
    # print(basic_strategy)
    return basic_strategy

def create_basic_strategy_no_double():
    basic_strategy = {}
    for i in range(17,22):
        for j in  DECK_VALUE:
            basic_strategy['hard ' + str(i) + ',' + j] = '-'
    for i in range(12,17):
        for j in  ['2', '3', '4', '5', '6']:
            basic_strategy['hard ' + str(i) + ',' + j] = '-'
        for j in  ['7', '8', '9', 'T', 'A']:
            basic_strategy['hard ' + str(i) + ',' + j] = 'H'
    basic_strategy['hard 12,2'] = 'H'
    basic_strategy['hard 12,3'] = 'H'
    for i in range(9,12):
        for j in  ['2', '3', '4', '5', '6', '7', '8', '9']:
            basic_strategy['hard ' + str(i) + ',' + j] = 'H'
    basic_strategy['hard 11,T'] = 'H'
    basic_strategy['hard 11,A'] = 'H'
    basic_strategy['hard 10,T'] = 'H'
    basic_strategy['hard 10,A'] = 'H'
    for i in range(5,10):
        for j in  DECK_VALUE:
            basic_strategy['hard ' + str(i) + ',' + j] = 'H'
    basic_strategy['hard 9,3'] = 'H'
    basic_strategy['hard 9,4'] = 'H'
    basic_strategy['hard 9,5'] = 'H'
    basic_strategy['hard 9,6'] = 'H'
    for j in ['2', '3', '4', '5', '6', '7', '8', '9', 'T']:
        basic_strategy['pair A,' + j] = 'S'
    basic_strategy['pair A,A'] = 'H'
    for j in DECK_VALUE:
        basic_strategy['pair T,' + j] = '-'
    for j in ['2', '3', '4', '5', '6', '8', '9']:
        basic_strategy['pair 9,' + j] = 'S'
    basic_strategy['pair 9,' + '7'] = '-'
    basic_strategy['pair 9,' + 'T'] = '-'
    basic_strategy['pair 9,' + 'A'] = '-'
    for j in ['2', '3', '4', '5', '6', '7', '8', '9']:
        basic_strategy['pair 8,' + j] = 'S'
    basic_strategy['pair 8,' + 'T'] = 'H'
    basic_strategy['pair 8,' + 'A'] = 'H'
    for j in ['2', '3', '4', '5', '6', '7']:
        basic_strategy['pair 7,' + j] = 'S'
    basic_strategy['pair 7,' + 'T'] = 'H'
    basic_strategy['pair 7,' + 'A'] = 'H'
    basic_strategy['pair 7,' + '8'] = 'H'
    basic_strategy['pair 7,' + '9'] = 'H'
    for j in ['2', '3', '4', '5', '6']:
        basic_strategy['pair 6,' + j] = 'S'
    basic_strategy['pair 6,' + 'T'] = 'H'
    basic_strategy['pair 6,' + 'A'] = 'H'
    basic_strategy['pair 6,' + '8'] = 'H'
    basic_strategy['pair 6,' + '9'] = 'H'
    basic_strategy['pair 6,' + '7'] = 'H'
    for j in ['2', '3', '4', '5', '6', '7', '8', '9']:
        basic_strategy['pair 5,' + j] = 'H'
    basic_strategy['pair 5,' + 'T'] = 'H'
    basic_strategy['pair 5,' + 'A'] = 'H'
    for j in DECK_VALUE:
        basic_strategy['pair 4,' + j] = 'H'
    basic_strategy['pair 4,' + '5'] = 'S'
    basic_strategy['pair 4,' + '6'] = 'S'
    for i in range(2, 4):
        for j in ['2', '3', '4', '5', '6', '7']:
            basic_strategy['pair ' + str(i) + ',' + j] = 'S'
        for j in ['8', '9', 'T', 'A']:
            basic_strategy['pair ' + str(i) + ',' + j] = 'H'
    for j in DECK_VALUE:
        basic_strategy['soft 21,' + j] = '-'
        basic_strategy['soft 20,' + j] = '-'
        basic_strategy['soft 19,' + j] = '-'
    for i in range(2, 8):
        for j in DECK_VALUE:
            basic_strategy['soft ' + str(11+i) + ',' + j] = 'H'
    basic_strategy['soft 18,2'] = '-'
    basic_strategy['soft 18,7'] = '-'
    basic_strategy['soft 18,8'] = '-'
    basic_strategy['soft 18,5'] = '-'
    basic_strategy['soft 18,6'] = '-'
    basic_strategy['soft 18,4'] = '-'
    basic_strategy['soft 18,3'] = '-'
    basic_strategy['soft 17,6'] = 'H'
    basic_strategy['soft 17,5'] = 'H'
    basic_strategy['soft 17,4'] = 'H'
    basic_strategy['soft 17,3'] = 'H'
    basic_strategy['soft 16,6'] = 'H'
    basic_strategy['soft 16,5'] = 'H'
    basic_strategy['soft 16,4'] = 'H'
    basic_strategy['soft 15,6'] = 'H'
    basic_strategy['soft 15,5'] = 'H'
    basic_strategy['soft 15,4'] = 'H'
    basic_strategy['soft 14,6'] = 'H'
    basic_strategy['soft 14,5'] = 'H'
    basic_strategy['soft 13,6'] = 'H'
    basic_strategy['soft 13,5'] = 'H'
    # print(basic_strategy)
    return basic_strategy

def create_basic_strategy_no_double_no_split():
    basic_strategy = {}
    for i in range(17,22):
        for j in  DECK_VALUE:
            basic_strategy['hard ' + str(i) + ',' + j] = '-'
    for i in range(12,17):
        for j in  ['2', '3', '4', '5', '6']:
            basic_strategy['hard ' + str(i) + ',' + j] = '-'
        for j in  ['7', '8', '9', 'T', 'A']:
            basic_strategy['hard ' + str(i) + ',' + j] = 'H'
    basic_strategy['hard 12,2'] = 'H'
    basic_strategy['hard 12,3'] = 'H'
    for i in range(9,12):
        for j in  ['2', '3', '4', '5', '6', '7', '8', '9']:
            basic_strategy['hard ' + str(i) + ',' + j] = 'H'
    basic_strategy['hard 11,T'] = 'H'
    basic_strategy['hard 11,A'] = 'H'
    basic_strategy['hard 10,T'] = 'H'
    basic_strategy['hard 10,A'] = 'H'
    for i in range(5,10):
        for j in  DECK_VALUE:
            basic_strategy['hard ' + str(i) + ',' + j] = 'H'
    basic_strategy['hard 9,3'] = 'H'
    basic_strategy['hard 9,4'] = 'H'
    basic_strategy['hard 9,5'] = 'H'
    basic_strategy['hard 9,6'] = 'H'
    for j in ['2', '3', '4', '5', '6', '7', '8', '9', 'T']:
        basic_strategy['pair A,' + j] = 'H'
    basic_strategy['pair A,A'] = 'H'
    for j in DECK_VALUE:
        basic_strategy['pair T,' + j] = '-'
    for j in ['2', '3', '4', '5', '6', '8', '9']:
        basic_strategy['pair 9,' + j] = '-'
    basic_strategy['pair 9,' + '7'] = '-'
    basic_strategy['pair 9,' + 'T'] = '-'
    basic_strategy['pair 9,' + 'A'] = '-'
    for j in ['2', '3', '4', '5', '6']:
        basic_strategy['pair 8,' + j] = '-'
    basic_strategy['pair 8,' + '7'] = 'H'
    basic_strategy['pair 8,' + '8'] = 'H'
    basic_strategy['pair 8,' + '9'] = 'H'
    basic_strategy['pair 8,' + 'T'] = 'H'
    basic_strategy['pair 8,' + 'A'] = 'H'
    for j in ['2', '3', '4', '5', '6']:
        basic_strategy['pair 7,' + j] = '-'
    basic_strategy['pair 7,' + 'T'] = 'H'
    basic_strategy['pair 7,' + 'A'] = 'H'
    basic_strategy['pair 7,' + '8'] = 'H'
    basic_strategy['pair 7,' + '9'] = 'H'
    basic_strategy['pair 7,' + '7'] = 'H'
    for j in ['4', '5', '6']:
        basic_strategy['pair 6,' + j] = '-'
    basic_strategy['pair 6,' + 'T'] = 'H'
    basic_strategy['pair 6,' + 'A'] = 'H'
    basic_strategy['pair 6,' + '8'] = 'H'
    basic_strategy['pair 6,' + '9'] = 'H'
    basic_strategy['pair 6,' + '7'] = 'H'
    basic_strategy['pair 6,' + '2'] = 'H'
    basic_strategy['pair 6,' + '3'] = 'H'
    for j in ['2', '3', '4', '5', '6', '7', '8', '9']:
        basic_strategy['pair 5,' + j] = 'H'
    basic_strategy['pair 5,' + 'T'] = 'H'
    basic_strategy['pair 5,' + 'A'] = 'H'
    for j in DECK_VALUE:
        basic_strategy['pair 4,' + j] = 'H'
    for i in range(2, 4):
        for j in DECK_VALUE:
            basic_strategy['pair ' + str(i) + ',' + j] = 'H'
    for j in DECK_VALUE:
        basic_strategy['soft 21,' + j] = '-'
        basic_strategy['soft 20,' + j] = '-'
        basic_strategy['soft 19,' + j] = '-'
    for i in range(2, 8):
        for j in DECK_VALUE:
            basic_strategy['soft ' + str(11+i) + ',' + j] = 'H'
    basic_strategy['soft 18,2'] = '-'
    basic_strategy['soft 18,7'] = '-'
    basic_strategy['soft 18,8'] = '-'
    basic_strategy['soft 18,5'] = '-'
    basic_strategy['soft 18,6'] = '-'
    basic_strategy['soft 18,4'] = '-'
    basic_strategy['soft 18,3'] = '-'
    basic_strategy['soft 17,6'] = 'H'
    basic_strategy['soft 17,5'] = 'H'
    basic_strategy['soft 17,4'] = 'H'
    basic_strategy['soft 17,3'] = 'H'
    basic_strategy['soft 16,6'] = 'H'
    basic_strategy['soft 16,5'] = 'H'
    basic_strategy['soft 16,4'] = 'H'
    basic_strategy['soft 15,6'] = 'H'
    basic_strategy['soft 15,5'] = 'H'
    basic_strategy['soft 15,4'] = 'H'
    basic_strategy['soft 14,6'] = 'H'
    basic_strategy['soft 14,5'] = 'H'
    basic_strategy['soft 13,6'] = 'H'
    basic_strategy['soft 13,5'] = 'H'
    # print(basic_strategy)
    return basic_strategy
