import re
from pathlib import Path

table = []
numbers = []
score = 0
file_path = Path("/home/empi/Advent_of_Code_2023/03/03_01/puzzle_input")


def add_line(line, tab):
    line = re.sub("\n", "", line)
    tab.append(line)


def check_number(table, score):
    counter = 0
    table_size = len(table)
    for line in table:
        prev_line = []
        next_line = []
        for match in re.finditer(r'[*]', line):
            line_length = len(line)
            prev = False
            next = False
            top = False
            bottom = False

            # Check if symbol before
            if match.span()[0] != 0 and line[match.span()[0] - 1].isdigit():
                prev = True

            # Check if symbol after
            if match.span()[1] != line_length and line[match.span()[1]].isdigit():
                next = True

            # Check if symbol in prev line
            if counter != 0:
                prev_line = table[counter - 1][match.span()[0] - 1:match.span()[1] + 1]
                for char in prev_line:
                    if char.isdigit():
                        top = True

            # Check if symbol in next line
            if counter != table_size - 1:
                if match.span()[0] == 0:
                    next_line = table[counter + 1][match.span()[0]:match.span()[1] + 1]
                else:
                    next_line = table[counter + 1][match.span()[0] - 1:match.span()[1] + 1]
                for char in next_line:
                    if char.isdigit():
                        bottom = True

            if (top + bottom + prev + next) == 2:
                #score += int(match.group())
                numbers.append(match.group())
                print(match.span(), line)
        counter += 1
    return score


with file_path.open(mode="r", encoding="utf-8") as file:
    line_counter = 0
    for line in file:
        add_line(line, table)
    score = check_number(table, score)
print(numbers)

