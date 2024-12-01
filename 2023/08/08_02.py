from pathlib import Path
import re
import math

file_path = Path("/home/empi/Advent_of_Code_2023/08/puzzle_input")


seq = "LLRRRLLRRRLRRRLRLRLLRRLRRRLLLRLRRRLRRRLRLLRRLRRRLLRRLRRLRLRRRLRRLLRLRRLRRRLRRLLRRRLRLLLRLRRRLRRLLLLRRRLRRRLRRRLRLRRLRRLRLRRLLRLLRRRLRRLRLLRRLRRLLRLLRLRRRLRLRLRRRLRRLLLRLRRRLLRLLRRRLRLRLRRRLLRLLLLRRRLRRRLRLRRRLRRLRRLLRLRLRRRLRRRLRLRRLLLLRLRRRLRRRLRLRRRLRLRRLRLRRRR"
move_seq = []
path = {}
no_of_paths = 0
starting_nodes = []


def find_finish(starting_node, counter, counter_len, results):
    score = 0
    current_pos = starting_node
    while True:
        next_move = move_seq[counter]
        if next_move == "R":
            current_pos = path[current_pos][1]
        else:
            current_pos = path[current_pos][0]

        score += 1

        if counter < counter_len - 1:
            counter += 1
        else:
            counter = 0

        if current_pos[2] == "Z":
            results.append(score)
            break

    return results


with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        line = re.sub(r'[^A-Z\s\d]', "", line)
        line = re.sub(r'  +', " ", line)
        line = re.sub(r"\n", "", line)
        line = re.split(" ", line)
        path[line[0]] = [line[1], line[2]]

for char in seq:
    move_seq.append(char)

for start, nodes in path.items():
    if start[2] == "A":
        starting_nodes.append(start)
        no_of_paths += 1

counter = 0
nmw = []
final_score = 1
counter_len = len(move_seq)

for point in starting_nodes:
    find_finish(point, counter, counter_len, nmw)

print(math.lcm(nmw[0], nmw[1], nmw[2], nmw[3], nmw[4], nmw[5]))
