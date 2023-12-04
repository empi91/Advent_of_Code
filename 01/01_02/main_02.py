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

index_list = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

file_path = Path("/home/empi/Advent_of_Code_2023/01/01_01/puzzle_input")

with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        first_index = [-1, -1]
        last_index = [-1, -1]
        for index in index_list:
            position = line.find(index)
            if position != -1:
                if first_index[0] == -1 and last_index[0] == -1:
                    first_index = [position, len(index)]
                    last_index = [position, len(index)]
                elif position < first_index[0]:
                    first_index = [position, len(index)]
                elif position > last_index[0]:
                    last_index = [position, len(index)]

        line = line[first_index[0]:first_index[0] + first_index[1]] + line[last_index[0]:last_index[0] + last_index[1]]



        print(line)
        print("____________")