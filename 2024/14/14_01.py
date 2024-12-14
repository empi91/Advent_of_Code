import re 

robots = []

tall, wide = 103, 101
no_of_seconds = 100
area = [['.' for x in range(wide)] for y in range(tall)]

q1, q2, q3, q4 = 0, 0, 0 ,0
score = 0

for line in open("puzzle_input").read().split("\n"):
    px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
    robots.append([py, px, vx, vy])

for r in robots:

    # check both robot coordintaes after X seconds
    # Place them on the area

    for i in range(no_of_seconds):
        # change coordinates
        r[0] += r[3]
        r[1] += r[2]
        # check if coordinates after the move aren't outisde of the area
        if r[0] < 0:
            r[0] = tall - (0 - r[0])
        elif r[0] > (tall - 1):
            r[0] = 0 + (r[0] - tall)
        
        if r[1] < 0:
            r[1] = wide - (0 - r[1])
        elif r[1] > (wide -1):
            r[1] = 0 + (r[1] - wide)

    if area[r[0]][r[1]] == '.': area[r[0]][r[1]] = 1
    else: area[r[0]][r[1]] += 1

mid_col = wide // 2
mid_row = tall // 2

for r, row in enumerate(area):
    for c, column in enumerate(row):
        if c == mid_col: row[c] = ' '
        if r == mid_row: row[c] = ' '

#Q1:
for i in range(tall // 2):
    for j in range(wide // 2):
        if type(area[i][j]) == int:
            q1 += area[i][j]

#Q2:
for i in range(tall // 2):
    for j in range(wide // 2, wide):
        if type(area[i][j]) == int:
            q2 += area[i][j]

#Q3:
for i in range(tall // 2, tall):
    for j in range(wide // 2):
        if type(area[i][j]) == int:
            q3 += area[i][j]

#Q4:
for i in range(tall // 2, tall):
    for j in range(wide // 2, wide):
        if type(area[i][j]) == int: 
            q4 += area[i][j]

score = q1 * q2 * q3 * q4
print(score)