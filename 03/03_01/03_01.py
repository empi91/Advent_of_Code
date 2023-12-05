import re
from pathlib import Path

table = []
file_path = Path.cwd() / "puzzle_input"


def add_line(line, tab):
    line = re.sub("\n", "", line)
    tab.append(line)


def check_number(table):
    for line in table:
        for match in re.finditer(r'[0-9]+', line):
            line_length = len(line)

            # Check if symbol before
            if match.span()[0] == 0:
                #nothing before
            else:
                if (match.span()[0] - 1) != ".":
                    #symbol before

            # Check if symbol after
            if match.span()[1] == line_length:
                #nothing after
            else:
                if (match.span()[1] + 1) != ".":
                    #symbol after

            # Check if symbol in prev line
            

    return 0


with file_path.open(mode="r", encoding="utf-8") as file:
    line_counter = 0
    for line in file:
        add_line(line, table)

    check_number(table)
print(table)
