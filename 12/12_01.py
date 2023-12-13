from pathlib import Path
import re

file_path = Path.cwd() / "puzzle_input"

springs = []
numbers = []


def resolve_line():
    for line in springs:
        index = springs.index(line)
        line_length = len(line)

    return 0


with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        line = re.split(" ", line)
        springs.append(line[0].strip())
        numbers.append(list(line[1].strip()))

for line in springs:
    print(line)

for line in numbers:
    print(line)
