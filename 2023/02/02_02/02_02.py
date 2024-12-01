from pathlib import Path
import re

red_cubes = 12
green_cubes = 13
blue_cubes = 14
score = 0

file_path = Path("/home/empi/Advent_of_Code_2023/02/02_01/puzzle_input")

with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        result = re.split(r'[:;]', line)
        red_req = 0
        blue_req = 0
        green_req = 0
        game_result = 0
        for game in range(len(result)):
            if game == 0:
                result[game] = result[game][5:]
            else:
                result[game] = re.split(r'[,]', result[game])
                for color in result[game]:
                    if color.find("red") != -1:
                        color = re.sub(r'[^0-9]+', '',color)
                        if int(color) > int(red_req):
                            red_req = color
                    elif color.find("blue") != -1:
                        color = re.sub(r'[^0-9]+', '',color)
                        if int(color) > int(blue_req):
                            blue_req = color
                    elif color.find("green") != -1:
                        color = re.sub(r'[^0-9]+', '',color)
                        if int(color) > int(green_req):
                            green_req = color
        game_result = int(red_req) * int(blue_req) * int(green_req)
        score += game_result

    print(score)
