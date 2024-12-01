from pathlib import Path
import time

score = 0

path_file = Path.cwd() / "puzzle_input"

with path_file.open(mode="r", encoding="utf-8") as file:

    for line in file:
        line_numbers = ""
        for letter in line:
            if letter.isdigit():
                line_numbers += letter
        if len(line_numbers) == 1:
            line_numbers = 2 * line_numbers
        line_length = len(line_numbers)
        number = int(line_numbers[0]) * 10 + int(line_numbers[line_length-1])
        score += number

    print(f"Score: {score}")


