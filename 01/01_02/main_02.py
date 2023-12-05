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
    score = 0
    for line in file:
        first_index = [-1, -1]
        last_index = [-1, -1]
        for index in index_list:
            for match in re.finditer(index, line):
                if first_index[0] == -1 and last_index[0] == -1:
                    first_index = [match.span()[0], len(index)]
                    last_index = [match.span()[0], len(index)]
                elif match.span()[0] < first_index[0]:
                    first_index = [match.span()[0], len(index)]
                elif match.span()[0] > last_index[0]:
                    last_index = [match.span()[0], len(index)]

        line = line[first_index[0]:first_index[0] + first_index[1]] + line[last_index[0]:last_index[0] + last_index[1]]

        for key, value in letters_dict.items():
            line = re.sub(key, str(value), line)
        print(line)
        print("________")

        value = int(line[0]) * 10 + int(line[1])
        score += value
    print(score)
