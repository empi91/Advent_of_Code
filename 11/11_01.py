import copy
from pathlib import Path
import re

file_path = Path.cwd() / "puzzle_input"

data = []
numbered_grid = []


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


def replace_hash(grid, numbered_grid):
    counter = 1
    for row in grid:
        new_row = ""
        for char in row:
            if char == "#":
                new_row += str(counter)
                counter += 1
            else:
                new_row += char
        numbered_grid.append(new_row)
    return counter


with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        data.append(list(line.strip()))

extend_rows(data)
transposed_list = list(map(list, zip(*data)))
extend_rows(transposed_list)
grid = list(map(list, zip(*transposed_list)))
counter = replace_hash(grid, numbered_grid)

for line in numbered_grid:
    print(line)