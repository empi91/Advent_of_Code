from pathlib import Path
import re

file_path = Path("/home/empi/Advent_of_Code_2023/09/puzzle_input")

history_data = []
final_score = 0


def calc_next_row(row):
    next = []
    length = len(row)
    for i in range(length - 1):
        next.append(int(row[i + 1]) - int(row[i]))
    return next


def calc_first_value(values):
    score = 0
    prev_value = 0
    values.pop(-1)
    length = len(values)

    for i in range(length):
        if i == 0:
            prev_value = values[-1]
        else:
            prev_value = values[-i - 1] - prev_value
    score = prev_value
    return score


with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        line = re.sub("\n", "", line)
        line = re.split(" ", line)
        history_data.append(line)

for history in history_data:
    first_values = []
    is_zeroed = False
    print(history)
    first_values.append(int(history[0]))
    next_row = calc_next_row(history)
    first_values.append(next_row[0])
    while not is_zeroed:
        only_zeroes = True
        print(next_row)
        for char in next_row:
            if char != 0:
                only_zeroes = False
        if sum(next_row) == 0 and only_zeroes:
            history_score = calc_first_value(first_values)
            final_score += history_score
            is_zeroed = True
        else:
            next_row = calc_next_row(next_row)
            first_values.append(next_row[0])
    print(first_values)
    print("___________")
print(final_score)
