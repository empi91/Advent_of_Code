from pathlib import Path

file_path = Path.cwd() / "puzzle_input"

data = []
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
                print(f"Row: {galaxy.index(row)} and column: {row.index(item)}")

    return 0


def calc_distances(coords, scor):
    count = 0
    for galaxy in coords:
        distance = 0
        index = coords.index(galaxy)
        row = galaxy[0]
        col = galaxy[1]
        for i in range(index + 1, len(coords)):
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
counter = replace_hash(grid)
check_galaxy_coordinates(grid)
score = calc_distances(galaxies_coords, score)

print(score)
