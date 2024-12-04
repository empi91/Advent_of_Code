import numpy as np

score = 0
rows = 0
cols = 0

with open("puzzle_input") as file:
    for line in file:
        rows += 1
        if cols == 0:
            cols = len(line.strip()) 


letters = np.empty((rows, cols), dtype='str')


with open("puzzle_input") as file:
    for x, line in enumerate(file):
        for y, letter in enumerate(line.strip()):
            letters[x][y] = letter

def check_center(a, b, cp):
    pair = (a, b)
    if pair not in cp:
        cp.append(pair)
        return 1
    else:
        return 0

def check_down_left(a, b, cp):
    if a <= rows - 3 and b >= 2:
        global score
        if letters[a+1][b-1] == "A":
            if letters[a+2][b-2] == "S":
                if (letters[a][b-2] == "M" and letters[a+2][b] == "S") or (letters[a][b-2] == "S" and letters[a+2][b] == "M"):
                    if check_center(a+1, b-1, cp):
                        score += 1
    else:
        pass

def check_down_right(a, b, cp):
    if a <= rows - 3 and b <= cols - 3:
        global score
        if letters[a+1][b+1] == "A":
            if letters[a+2][b+2] == "S":
                if (letters[a][b+2] == "M" and letters[a+2][b] == "S") or (letters[a][b+2] == "S" and letters[a+2][b] == "M"):
                    if check_center(a+1, b+1, cp):
                        score += 1
    else:
        pass

def check_up_left(a, b, cp):
    if a >= 2 and b >= 2:
        global score
        if letters[a-1][b-1] == "A":
            if letters[a-2][b-2] == "S":
                if (letters[a][b-2] == "M" and letters[a-2][b] == "S") or (letters[a][b-2] == "S" and letters[a-2][b] == "M"):
                    if check_center(a-1, b-1, cp):
                        score += 1
    else:
        pass

def check_up_right(a, b, cp):
    if a >= 2 and b <= cols - 3:
        global score
        if letters[a-1][b+1] == "A":
            if letters[a-2][b+2] == "S":
                if (letters[a][b+2] == "M" and letters[a-2][b] == "S") or (letters[a][b+2] == "S" and letters[a-2][b] == "M"):
                    if check_center(a-1, b+1, cp):
                        score += 1
    else:
        pass

cp = []

for x in range(rows):
    for y in range(cols):
        if letters[x][y] == "M":
            check_up_left(x, y, cp)
            check_up_right(x, y, cp)
            check_down_left(x, y, cp)
            check_down_right(x, y, cp)

print(score)
print(cp)
