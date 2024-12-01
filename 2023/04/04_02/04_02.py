from pathlib import Path
import re
import os

file_path_original = Path("/home/empi/Advent_of_Code_2023/04/04_01/puzzle_input")

score = 0
copies_number = []
cards = []

with file_path_original.open(mode="r", encoding="utf-8") as file:
    for line in file:
        card_no = 0
        card_value = 0
        card_winning = []
        card_numbers = []
        line = re.sub("\n", "", line)
        line = re.sub(r'\s{2,3}', " ", line)
        sliced_line = re.split(r'[:|]', line)
        for count, part in enumerate(sliced_line):
            if count == 0:
                part = re.sub(r'\D', '', part)
                card_no = int(part)
            elif count == 1:
                win_numbers = re.split(" ", part)
                for num in win_numbers:
                    if num.isdigit():
                        card_winning.append(int(num))
            else:
                card_num = re.split(" ", part)
                for num in card_num:
                    if num.isdigit():
                        card_numbers.append(int(num))
        for number in card_winning:
            if number in card_numbers:
                card_value += 1
        copies_number.append([card_no, card_value, 1])
        cards.append(line)

for card in copies_number:
    for i in range(card[0], card[0] + card[1], 1):
        copies_number[i][2] += 1 * card[2]

score = 0
for card in copies_number:
    score += card[2]

print(score)
