import copy
from pathlib import Path
import re

file_path = Path.cwd() / "puzzle_input"

data = []
numbered_grid = []
galaxies_coords = []
score = 0

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
        numbered_grid.append(list(new_row))
    return counter - 1


def check_galaxy_coordinates(galaxy):
    for row in galaxy:
        for item in row:
            if item.isdigit():
                galaxies_coords.append([galaxy.index(row), row.index(item)])

    return 0


def calc_distances(coords, scor):
    count = 0
    for galaxy in coords:
        distance = 0
        index = coords.index(galaxy)
        row = galaxy[0]
        col = galaxy[1]
        for i in range(index + 1, len(coords)):
            print(f"Pair: {numbered_grid[row][col]} and {numbered_grid[coords[i][0]][coords[i][1]]}")
            distance += abs(coords[i][0] - row)
            distance += abs(coords[i][1] - col)
            count += 1
        scor += distance
    print(count)
    return scor


with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        data.append(list(line.strip()))

extend_rows(data)
transposed_list = list(map(list, zip(*data)))
extend_rows(transposed_list)
grid = list(map(list, zip(*transposed_list)))
# counter = replace_hash(grid, numbered_grid)
# check_galaxy_coordinates(numbered_grid)
# score = calc_distances(galaxies_coords, score)

for line in grid:
    print(line)

# print(galaxies_coords)
# print(counter)
print(score)