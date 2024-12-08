import math
from collections import defaultdict

score = 0

area = []
antennas = defaultdict(list)


with open('puzzle_input') as file:
    for line in file:
        area.append(list(line.strip()))


for i, row in enumerate(area):
    for j, column in enumerate(area[i]):
        if area[i][j] != '.':
            if not antennas[area[i][j]]:
                antennas[area[i][j]] = [(i, j)]
            else:
                antennas[area[i][j]].append((i, j))


for antenna_type, antenna_locations in antennas.items():
    for location in antenna_locations:
        for item in antenna_locations:
            if math.dist(location, item) != 0:
                y_diff = location[1] - item[1]
                x_diff = location[0] - item[0]
                if (location[0] + x_diff) in range(0, len(area)) and (location[1] + y_diff) in range(len(area[0])):
                    area[location[0]+ x_diff][location[1] + y_diff] = "#" 



for line in area:
    for i in line:
        if i == '#': score += 1

print(score)