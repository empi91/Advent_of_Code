from pathlib import Path
import re
import copy

file_path = Path.cwd() / "puzzle_input"
pipes = []
path_length = []

counter = 0

is_finished = False


def north_south():
    print("North-South")
    return 0
def east_west():
    print("East-West")

    return 0
def north_east():

    return 0
def north_west():

    return 0
def south_west():

    return 0
def south_east():

    return 0
def ground():
    print("Ground")
    return 0


def check_symbol_around(symbol):
    for key, value in pipes_dict.items():
        if symbol == key:
            pipes_dict[key]()
    return 0


pipes_dict = {
    "|": north_south,
    "-": east_west,
    "L": north_east,
    "J": north_west,
    "7": south_west,
    "F": south_east,
    ".": ground,
}


with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        line = re.sub("\n", "", line)
        pipes.append(line)

path_length = copy.deepcopy(pipes)
path_length = [item.replace("S", "0") for item in path_length]

while not is_finished:
    starting_point = []

    for line in path_length:
        for char in line:
            if char.isdigit():
                if int(char) == counter:
                    starting_point.append([path_length.index(line), line.index(char)])

    for item in starting_point:
        point_north = path_length[item[0] - 1][item[1]]
        point_south = path_length[item[0] + 1][item[1]]
        point_west = path_length[item[0]][item[1] - 1]
        point_east = path_length[item[0]][item[1] + 1]

        check_symbol_around(point_north)
        check_symbol_around(point_south)
        check_symbol_around(point_east)
        check_symbol_around(point_west)

    counter += 1
    is_finished = True


print(f" {point_north}")
print(f"{point_west} {point_east}")
print(f" {point_south}")
