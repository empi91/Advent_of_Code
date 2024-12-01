from pathlib import Path
import re

red_cubes = 12
green_cubes = 13
blue_cubes = 14
score = 0

file_path = Path.cwd() / "puzzle_input"

with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        result = re.split(r'[:;]', line)
        game_ok = True
        for game in range(len(result)):
            if game == 0:
                result[game] = result[game][5:]
            else:
                result[game] = re.split(r'[,]', result[game])
                for color in result[game]:
                    if color.find("red") != -1:
                        color = re.sub(r'[^0-9]+', '',color)
                        if int(color) > red_cubes:
                            game_ok = False
                    elif color.find("blue") != -1:
                        color = re.sub(r'[^0-9]+', '',color)
                        if int(color) > blue_cubes:
                            game_ok = False
                    elif color.find("green") != -1:
                        color = re.sub(r'[^0-9]+', '',color)
                        if int(color) > green_cubes:
                            game_ok = False
        if game_ok:
            score += int(result[0])

    print(score)
