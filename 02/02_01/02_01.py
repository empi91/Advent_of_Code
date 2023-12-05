from pathlib import Path

red_cubes = 12
green_cubes = 13
blue_cubes = 14

file_path = Path.cwd() / "puzzle_input"

with file_path.open(mode="r", encoding="utf-8") as file:
    for line in file:
        
