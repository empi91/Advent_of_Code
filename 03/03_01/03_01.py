import re
from pathlib import Path

table = []
file_path = Path.cwd() / "puzzle_input"


def add_line(line, tab):
    line = re.sub("\n", "", line)
    tab.append([line])


def check_number(table):
    for line in table:
        print(line)
    return 0


with file_path.open(mode="r", encoding="utf-8") as file:
    line_counter = 0
    for line in file:
        add_line(line, table)
        
    check_number(table)

