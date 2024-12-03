import re

score = 0

with open("puzzle_input") as file:
    memory = file.read().split("mul(")

    for block in memory:
        if re.match("\d+,\d+\)", block):
            numbers = re.findall(r"\d+,\d+\)", block)
            a, b = map(int, numbers[0].replace(")", "").split(","))
            score += a * b



print(score)



