from pathlib import Path
import re

file_path= Path.cwd() / "puzzle_input"
history_data = []


def calc_next_row(row):
    next_row = []
    length = len(history)
    for i in range(length - 1):
        next_row.append(int(history[i + 1]) - int(history[i]))

    return next_row


with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        line = re.sub("\n", "", line)
        line = re.split(" ", line)
        history_data.append(line)

print(history_data)

for history in history_data:
    is_zeroed = False
    next_row = calc_next_row(history)

    while not is_zeroed:
        if sum(next_row) == 0:
            is_zeroed = True
        else:
            next_row = calc_next_row(next_row)

    print(sum(next_row))



