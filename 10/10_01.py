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
    symbol = path_length[row][index]
    if direction == "north":
        if symbol in symbols_north:
            path_length[row] = path_length[row][:index] + str(counter + 1) + path_length[row][index + 1:]
            return True
    elif direction == "south":
        if symbol in symbols_south:
            path_length[row] = path_length[row][:index] + str(counter + 1) + path_length[row][index + 1:]
            return True
    elif direction == "west":
        if symbol in symbols_west:
            path_length[row] = path_length[row][:index] + str(counter + 1) + path_length[row][index + 1:]
            return True
    elif direction == "east":
        if symbol in symbols_east:
            path_length[row] = path_length[row][:index] + str(counter + 1) + path_length[row][index + 1:]
            return True
    return False


with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        line = re.sub("\n", "", line)
        pipes.append(line)

path_length = copy.deepcopy(pipes)
path_length = [item.replace("S", "0") for item in path_length]

while not is_finished:
    starting_point = []
    was_changed = []

    for line in path_length:
        for char in line:
            if char.isdigit():
                if counter != 7:
                    if int(char) == counter:
                        starting_point.append([path_length.index(line), line.index(char)])
                if counter == 7:
                    if int(char) == counter and pipes[path_length.index(line)][line.index(char)] == "7":
                        starting_point.append([path_length.index(line), line.index(char)])
                    else:
                        continue

    for item in starting_point:
        if item[0] == 0:
            #dont check north
            was_changed.append(check_symbol_around(item[0] + 1, item[1], counter, "south"))
            was_changed.append(check_symbol_around(item[0], item[1] - 1, counter, "west"))
            was_changed.append(check_symbol_around(item[0], item[1] + 1, counter, "east"))
        elif item[0] == len(path_length) - 1:
            #dont check south
            was_changed.append(check_symbol_around(item[0] - 1, item[1], counter, "north"))
            was_changed.append(check_symbol_around(item[0], item[1] - 1, counter, "west"))
            was_changed.append(check_symbol_around(item[0], item[1] + 1, counter, "east"))
        elif item[1] == 0:
            #dont check west
            was_changed.append(check_symbol_around(item[0] - 1, item[1], counter, "north"))
            was_changed.append(check_symbol_around(item[0] + 1, item[1], counter, "south"))
            was_changed.append(check_symbol_around(item[0], item[1] + 1, counter, "east"))
        elif item[1] == len(path_length[0]) - 1:
            #dont check east
            was_changed.append(check_symbol_around(item[0] - 1, item[1], counter, "north"))
            was_changed.append(check_symbol_around(item[0] + 1, item[1], counter, "south"))
            was_changed.append(check_symbol_around(item[0], item[1] - 1, counter, "west"))
        else:
            was_changed.append(check_symbol_around(item[0] - 1, item[1], counter, "north"))
            was_changed.append(check_symbol_around(item[0] + 1, item[1], counter, "south"))
            was_changed.append(check_symbol_around(item[0], item[1] - 1, counter, "west"))
            was_changed.append(check_symbol_around(item[0], item[1] + 1, counter, "east"))

    counter += 1
    if sum(was_changed) == 0:
        is_finished = True
        print(f"Score: {counter - 1}")

# for line in path_length:
#     print(line)