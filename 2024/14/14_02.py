import re 
from copy import deepcopy
robots = []

tall, wide = 103, 101
area = [[0 for x in range(wide)] for y in range(tall)]

score = 0
mid_col = wide // 2
mid_row = tall // 2

for line in open("puzzle_input").read().split("\n"):
    px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
    robots.append([py, px, vx, vy])

overleap = True
while overleap:
    overleap = False
    a1 = deepcopy(area)
    for r in robots:
        r[0] += r[3]
        r[1] += r[2]
        if r[0] < 0:
            r[0] = tall - (0 - r[0])
        elif r[0] > (tall - 1):
            r[0] = 0 + (r[0] - tall)
        
        if r[1] < 0:
            r[1] = wide - (0 - r[1])
        elif r[1] > (wide -1):
            r[1] = 0 + (r[1] - wide)

        a1[r[0]][r[1]] += 1

    for r, row in enumerate(a1):
        for c, column in enumerate(row):
            if a1[r][c] > 1: overleap = True


    score += 1

# for r, row in enumerate(a1):
#     for c, column in enumerate(row):
#         if c == mid_col: row[c] = ' '
#         if r == mid_row: row[c] = ' '

for row in a1:
    print(*row, sep="")
print(score)
