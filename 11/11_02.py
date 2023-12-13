from pathlib import Path

file_path = Path.cwd() / "puzzle_input"

data = []
galaxies_coords = []
score = 0
expand_factor = 1000000


def extend_rows(grid):
    start_search = 0
    for row in grid:
        if all(char == "." or char == "|" for char in row):
            try:
                start_search = grid.index(row, start_search + 2)
                new_row = len(row) * "|"
                grid.insert(start_search, new_row)
            except ValueError:
                continue
    return 0


def replace_hash(grid):
    counter = 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                grid[i][j] = counter
                counter += 1
    return 0


def check_galaxy_coordinates(galaxy):
    for row in galaxy:
        for item in row:
            if str(item).isdigit():
                galaxies_coords.append([galaxy.index(row), row.index(item)])
    return 0


def check_black_hole(start_row, start_col, end_row, end_col):
    path = []
    number = 0
    if end_col >= start_col:
        for i in range(start_col + 1, end_col + 1):
            path.append(grid[start_row][i])
    else:
        for i in range(start_col - 1, end_col - 1, -1):
            path.append(grid[start_row][i])

    if end_row >= start_row:
        for j in range(start_row + 1, end_row):
            path.append(grid[j][end_col])
    else:
        for j in range(start_row - 1, end_row, -1):
            path.append(grid[j][end_col])

    for char in path:
        if char == "|":
            number += 1

    return number


def calc_distances(coords, scor):
    count = 0
    for galaxy in coords:
        distance = 0
        index = coords.index(galaxy)
        row = galaxy[0]
        col = galaxy[1]
        for i in range(index + 1, len(coords)):
            # print(f"Pair: {grid[row][col]} and {grid[coords[i][0]][coords[i][1]]}")
            distance += abs(coords[i][0] - row) + abs(coords[i][1] - col)
            multiplier = check_black_hole(row, col, coords[i][0], coords[i][1])
            distance = distance - (2 * multiplier) + (multiplier * expand_factor)
            count += 1
        scor += distance
    return scor


with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        data.append(list(line.strip()))

extend_rows(data)
transposed_list = list(map(list, zip(*data)))
extend_rows(transposed_list)
grid = list(map(list, zip(*transposed_list)))
counter = replace_hash(grid)
check_galaxy_coordinates(grid)
score = calc_distances(galaxies_coords, score)

print(score)
