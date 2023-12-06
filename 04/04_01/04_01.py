from pathlib import Path
import re

file_path = Path.cwd() / "puzzle_input"

score = 0

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
                if card_value == 0:
                    card_value = 1
                else:
                    card_value = 2 * card_value
        score += card_value
print(score)



