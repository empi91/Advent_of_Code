from pathlib import Path
import re

file_path = Path.cwd() / "puzzle_input"

seq = "LLRRRLLRRRLRRRLRLRLLRRLRRRLLLRLRRRLRRRLRLLRRLRRRLLRRLRRLRLRRRLRRLLRLRRLRRRLRRLLRRRLRLLLRLRRRLRRLLLLRRRLRRRLRRRLRLRRLRRLRLRRLLRLLRRRLRRLRLLRRLRRLLRLLRLRRRLRLRLRRRLRRLLLRLRRRLLRLLRRRLRLRLRRRLLRLLLLRRRLRRRLRLRRRLRRLRRLLRLRLRRRLRRRLRLRRLLLLRLRRRLRRRLRLRRRLRLRRLRLRRRR"
move_seq = []
path = {}

with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        line = re.sub(r'[^A-Z\s]', "", line)
        line = re.sub(r'  +', " ", line)
        line = re.sub(r"\n", "", line)
        line = re.split(" ", line)
        path[line[0]] = [line[1], line[2]]
print(path)
for char in seq:
    move_seq.append(char)

current_pos = "AAA"

counter = 0
counter_len = len(move_seq)

score = 0

while True:
    next_move = move_seq[counter]
    current_index = list(path).index(current_pos)

    if next_move == "R":
        current_pos = path[current_pos][1]
    else:
        current_pos = path[current_pos][0]
    score += 1

    if counter < counter_len - 1:
        counter += 1
    else:
        counter = 0

    if current_pos == "ZZZ":
        print(score)
        exit()