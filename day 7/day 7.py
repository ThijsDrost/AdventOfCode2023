from functools import cmp_to_key

loc = r'input.txt'
hand_values1 = {'A': 1, 'K': 2, 'Q': 3, 'J': 4, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12,
                '2': 13}
hand_values2 = {'A': 1, 'K': 2, 'Q': 3, 'T': 5, '9': 6, '8': 7, '7': 8, '6': 9, '5': 10, '4': 11, '3': 12,
                '2': 13, 'J': 14}


def identifier(hand: str, joker: bool):
    if joker:
        stripped_hand = hand.replace('J', '')
    else:
        stripped_hand = hand
    hand_set = set(stripped_hand)
    if len(hand_set) in (0, 1):
        return 1
    if len(hand_set) == 2:
        if len(stripped_hand) <= 3:
            return 2
        if len(stripped_hand) == 4:
            if hand.count(stripped_hand[0]) == 2:
                return 3
            return 2
        if hand.count(stripped_hand[0]) == 1 or hand.count(stripped_hand[0]) == 4:
            return 2
        return 3
    if len(hand_set) == 3:
        if len(stripped_hand) in (3, 4):
            return 4
        for card in hand_set:
            if hand.count(card) == 3:
                return 4
        return 5
    if len(hand_set) == 4:
        return 6
    return 7


def comparer(hand1, hand2, hand_values):
    if hand1[0] > hand2[0]:
        return -1
    if hand1[0] < hand2[0]:
        return 1
    for card1, card2 in zip(hand1[1], hand2[1]):
        if hand_values[card1] > hand_values[card2]:
            return -1
        if hand_values[card1] < hand_values[card2]:
            return 1
    return 0


for h_v, jok in zip((hand_values1, hand_values2), (False, True)):
    values = [(identifier(line.split()[0], jok), line.split()[0], int(line.split()[1])) for line in open("input.txt").read().split("\n") if line]
    values.sort(key=cmp_to_key(lambda x, y: comparer(x, y, h_v)))
    total = 0
    for i in range(len(values)):
        total += values[i][2] * (i + 1)
    print(total)
