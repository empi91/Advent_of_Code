from pathlib import Path
import re

file_path= Path.cwd() / "puzzle_input"
history_data = []
final_score = 0


def calc_next_row(row):
    next = []
    length = len(row)
    for i in range(length - 1):
        next.append(int(row[i + 1]) - int(row[i]))
    return next


with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        line = re.sub("\n", "", line)
        line = re.split(" ", line)
        history_data.append(line)

for history in history_data:
    is_zeroed = False
    extr_value = int(history[-1])
    print(history)
    next_row = calc_next_row(history)
    extr_value += next_row[-1]
    while not is_zeroed:
        only_zeroes = True
        print(next_row)
        for char in next_row:
            if char != 0:
                only_zeroes = False
        if sum(next_row) == 0 and only_zeroes:
            is_zeroed = True
        else:
            next_row = calc_next_row(next_row)
            extr_value += next_row[-1]

    final_score += extr_value
    print(extr_value)
    print("___________")
print(final_score)



