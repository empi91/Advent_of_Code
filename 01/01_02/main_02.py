from pathlib import Path
import re

letters_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

file_path = Path("/home/empi/Advent_of_Code_2023/01/01_01/puzzle_input")


def check_replace_string(line):
    id_numbers = []
    for key in letters_dict:
        id_numbers.append(re.findall(key, line))
        # if line.find(key) > -1:
        #     id_numbers[key] = [line.find(key), len(key)]
            # key_length = len(key)
            # word = line[line.find(key):line.find(key) + key_length]
            #
            # prefix = line[:line.find(key)]
            # number = str(letters_dict[key])
            # suffix = line[line.find(key) + key_length:]
            #
            # new_line = prefix + number + suffix
            # print(new_line)
    print(id_numbers)
    print("_________________")
    return line


with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        check_replace_string(line)
        #print(line)
