from pathlib import Path
import re
import copy

file_path = Path.cwd() / "puzzle_input"
pipes = []
path_length = []

symbols_north = ["|", "7", "F"]
symbols_south = ["|", "L", "J"]
symbols_west = ["-", "L", "F"]
symbols_east = ["-", "J", "7"]

counter = 0

is_finished = False


def check_symbol_around(row, index, count, direction):
    # symbol = pipes[row][index]
    symbol = path_length[row][index]
    if direction == "north":
        if symbol in symbols_north:
            path_length[row] = path_length[row][:index] + str(counter + 1) + path_length[row][index + 1:]
            # print(f"North would be replaced with {counter}")
    elif direction == "south":
        if symbol in symbols_south:
            path_length[row] = path_length[row][:index] + str(counter + 1) + path_length[row][index + 1:]
            # print(f"South would be replaced with {counter}")
    elif direction == "west":
        if symbol in symbols_west:
            path_length[row] = path_length[row][:index] + str(counter + 1) + path_length[row][index + 1:]
            # print(f"West would be replaced with {counter}")
    elif direction == "east":
        if symbol in symbols_east:
            path_length[row] = path_length[row][:index] + str(counter + 1) + path_length[row][index + 1:]
            # print(f"East would be replaced with {counter}")
    return 0


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
        check_symbol_around(item[0] - 1, item[1], counter, "north")
        check_symbol_around(item[0] + 1, item[1], counter, "south")
        check_symbol_around(item[0], item[1] - 1, counter, "west")
        check_symbol_around(item[0], item[1] + 1, counter, "east")

    counter += 1
    if counter == 5:
        is_finished = True

for line in path_length:
    print(line)