import copy
from pathlib import Path
import re

file_path = Path.cwd() / "puzzle_input"

data = []
row_indexes = []
data_numbers = []
galaxy_indexes = []

counter = 1


def extend_rows(grid):
    start_search = 0
    for row in grid:
        if all(char == "." for char in row):
            try:
                start_search = grid.index(row, start_search + 2)
                grid.insert(start_search, row)
            except ValueError:
                continue
    return 0


def extend_columns(map, extended_map):
    ext_row_no = len(extended_map)

    for i in range(len(map[0])):
        is_empty = True
        for j in range(len(map)):
            if map[j][i] == "#":
                is_empty = False
                break
        if is_empty:
            for j in range(ext_row_no):
                print(f"{j}, {i}")
                # extended_map[j] = extended_map[j][:i] + "." + extended_map[j][i:]
    return 0


with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        data.append(list(line.strip()))

extend_rows(data)
data_numbers = copy.deepcopy(data)
extend_columns(data, data_numbers)

# for row in data:
#     new_row = ""
#     for char in row:
#         if char == "#":
#             new_row += str(counter)
#             counter += 1
#         else:
#             new_row += char
#     data_numbers.append(new_row)



print("____")
for line in data:
    print(line)