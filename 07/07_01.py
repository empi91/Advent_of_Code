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


def check_hand_type(hand):
    if check_how_many_card_identical(hand):
        type = five_of_a_kind
    elif four_the_same:
        type = four_of_a_kind
    elif three_the_same and two_the_same:
        type = full_house
    elif two_the_same and two_the_same:
        type = two_pair
    elif two_the_same:
        type = one_pair
    elif all_cards_distinct:
        type = high_card

    return 0


def check_how_many_card_identical(hand):
    is_five = False
    is_four = False
    is_full_house = False
    is_three = False
    is_two = False
    is_one = False
    is_high = False

    symbols_in_hand = []
    print(hand[0])
    # Split hand into separate symbols
    for char in hand[0]:
        symbols_in_hand.append([char, 0])
    print(symbols_in_hand)

    # Count how many times each symbol is present in hand
    for symbol in symbols_in_hand:
        symbol[1] = hand[0].count(symbol[0])

    # Remove duplicates
    unique_symbols_in_hand = []
    [unique_symbols_in_hand.append(x) for x in symbols_in_hand if x not in unique_symbols_in_hand]
    print(unique_symbols_in_hand)

    for symbol in unique_symbols_in_hand:
        if symbol[1] == 5:
            is_five = True
        elif symbol[1] == 4:
            is_four = True
        elif symbol[1] == 3:
            is_three = True

    return 0


def check_hand_strength(hand):

    return 0


def hands_sort(all_hands):
    length = len(all_hands)
    is_sorted = False
    while not is_sorted:
        changed = 0
        for i in range(length - 1):
            if check_hand_type(all_hands[i]) > check_hand_type(all_hands[i + 1]):
                temp = all_hands[i + 1]
                all_hands[i] = all_hands[i + 1]
                all_hands[i + 1] = temp
                changed = 1
            elif check_hand_type(all_hands[i]) == check_hand_type(all_hands[i + 1]):
                if check_hand_strength(all_hands[i]) > check_hand_strength(all_hands[i + 1]):
                    temp = all_hands[i + 1]
                    all_hands[i] = all_hands[i + 1]
                    all_hands[i + 1] = temp
                    changed = 1
        if changed == 0:
            is_sorted = True
    return 0


hands_sort(hands)
