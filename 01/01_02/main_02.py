from pathlib import Path

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
    for key in letters_dict:
        if line.find(key) > -1:
            key_length = len(key)
            word = line[line.find(key):line.find(key) + key_length]
            #line.replace(word, str(letters_dict[key]))
            print(f"Replacing: {word} with {letters_dict[key]}")
            #print(line[line.find(key):])
            #print(line[:line.find(key) + key_length])
            print(line)
    return line


with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        check_replace_string(line)
        #print(line)
