from pathlib import Path
import re

file_path = Path("/home/empi/Advent_of_Code_2023/04/04_01/puzzle_input")

score = 0
copies_number = []
cards = []

with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        card_no = 0
        card_value = 0
        card_winning = []
        card_numbers = []
        line = re.sub("\n", "", line)
        sliced_line = re.split(r'[:|]', line)
        for count, part in enumerate(sliced_line):
            if count == 0:
                for char in part:
                    if char.isdigit():
                        card_no = int(char)
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
        copies_number.append([card_no, card_value])
        cards.append(line)
print(copies_number)
# print(cards)

for item in copies_number:
    for i in range(1, item[1] + 1):
        card_name = "Card " + str(item[0] + i)
        for sequence in cards:
            if re.match(card_name, sequence):
                index = cards.index(sequence)
                cards.insert(index, sequence)
                break


for item in cards:
    print(item)
print(len(cards))
