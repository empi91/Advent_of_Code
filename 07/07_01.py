from pathlib import Path
import re

file_path = Path.cwd() / "puzzle_input"
hands = []

with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        line = re.sub("\n", "", line)
        line = re.split(r'\s', line)
        line.append("0")
        hands.append(line)

char_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def check_hand_type(hand):
    check_how_many_card_identical(hand)
    print(hand[0])
    if hand[2] == 7:
        print("five_of_a_kind")
    elif hand[2] == 6:
        print("four_of_a_kind")
    elif hand[2] == 5:
        print("full_house")
    elif hand[2] == 4:
        print("three_of_kind")
    elif hand[2] == 3:
        print("two_pair")
    elif hand[2] == 2:
        print("one_pair")
    elif hand[2] == 1:
        print("high_card")
    return 0


def check_how_many_card_identical(hand):
    is_five = False
    is_four = False
    is_three = False
    is_two = False
    is_second_two = False
    is_one = False

    symbols_in_hand = []
    # Split hand into separate symbols
    for char in hand[0]:
        symbols_in_hand.append([char, 0])

    # Count how many times each symbol is present in hand
    for symbol in symbols_in_hand:
        symbol[1] = hand[0].count(symbol[0])

    # Remove duplicates
    unique_symbols_in_hand = []
    [unique_symbols_in_hand.append(x) for x in symbols_in_hand if x not in unique_symbols_in_hand]

    # Check how many card identical
    for symbol in unique_symbols_in_hand:
        if symbol[1] == 5:
            is_five = True
        elif symbol[1] == 4:
            is_four = True
        elif symbol[1] == 3:
            is_three = True
        elif symbol[1] == 2 and not is_two:
            is_two = True
        elif symbol[1] == 2 and is_two:
            is_second_two = True
        elif symbol[1] == 1:
            is_one = True

    if is_five:
        hand[2] = 7
    elif is_four:
        hand[2] = 6
    elif is_three and is_two:
        hand[2] = 5
    elif is_three:
        hand[2] = 4
    elif is_two and is_second_two:
        hand[2] = 3
    elif is_two:
        hand[2] = 2
    if is_one and (is_five + is_four + is_three + is_two) == 0:
        hand[2] = check_order(hand)
    return 0


def check_order(hand):
    first_char = hand[0][0]
    if first_char in char_order:
        index = char_order.index(first_char)
        if index > 9:
            return 0
        else:
            for i in range(1, 5):
                char = hand[0][i]
                next_char = char_order[index + i]
                if char != next_char:
                    return 0
            return 1
    return 0


def check_hand_strength(first_hand, second_hand):
    for i in range(5):
        first = first_hand[0][i]
        second = second_hand[0][i]
        first_index = char_order.index(first)
        second_index = char_order.index(second)
        if first_index < second_index:
            return 1
        elif first_index > second_index:
            return 0
        elif first_index == second_index:
            continue
    return None


def hands_sort(all_hands):
    length = len(all_hands)
    is_sorted = False
    while not is_sorted:
        changed = 0
        for i in range(length - 1):
            ita = all_hands[i]
            ita_plus_one = all_hands[i + 1]
            if all_hands[i][2] > all_hands[i + 1][2]:
                temp = all_hands[i]
                all_hands[i] = all_hands[i + 1]
                all_hands[i + 1] = temp
                changed = 1
            elif all_hands[i][2] == all_hands[i + 1][2]:
                if check_hand_strength(all_hands[i], all_hands[i + 1]):
                    temp = all_hands[i]
                    all_hands[i] = all_hands[i + 1]
                    all_hands[i + 1] = temp
                    changed = 1
        if changed == 0:
            is_sorted = True
    return 0


def count_score(all_hands):
    score = 0
    for rank, hand in enumerate(all_hands):
        score += int(hand[1]) * (rank + 1)
    print(score)
    

for hand in hands:
    check_how_many_card_identical(hand)

hands_sort(hands)
count_score(hands)