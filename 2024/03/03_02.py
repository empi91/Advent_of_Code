import re

score = 0
combined_pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
instructions = []
enabled = True

with open("puzzle_input") as file:
    text = file.read()

for match in re.finditer(combined_pattern, text):
    instructions.append(match[0])


for instruction in instructions: 
    if instruction.startswith("do()"):
        enabled = True

    elif instruction.startswith("don't"):
        enabled = False

    elif instruction.startswith("mul") and enabled:
        mul = re.findall(r"\d+,\d+", instruction)[0]
        a, b = map(int, mul.replace(")", "").split(","))
        score += a * b


print(score)






