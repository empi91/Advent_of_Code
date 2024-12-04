import numpy as np

score = 0

# First determine dimensions
rows = 0
cols = 0
with open("puzzle_input") as file:
    for line in file:
        rows += 1
        if cols == 0:
            cols = len(line.strip())  # remove trailing newline

# Create array with determined size
letters = np.empty((rows, cols), dtype='str')

# Fill array with letters
with open("puzzle_input") as file:
    for x, line in enumerate(file):
        for y, letter in enumerate(line.strip()):
            letters[x][y] = letter

def check_up(a, b):
    global score
    if a >= 3:
        if letters[a-1][b] == "M":
            if letters[a-2][b] == "A":
                if letters[a-3][b] == "S":
                    # print(f"{letters[a][b]}{letters[a-1][b]}{letters[a-2][b]}{letters[a-3][b]}")
                    score += 1
    else:
        pass

def check_down(a, b):
    if a <= rows - 4:
        global score
        if letters[a+1][b] == "M":
            if letters[a+2][b] == "A":
                if letters[a+3][b] == "S":
                    # print(f"{letters[a][b]}{letters[a+1][b]}{letters[a+2][b]}{letters[a+3][b]}")
                    score += 1
    else:
        pass
    

def check_left(a, b):
    if b >= 3:
        global score
        if letters[a][b-1] == "M":
            if letters[a][b-2] == "A":
                if letters[a][b-3] == "S":
                    # print(f"{letters[a][b]}{letters[a][b-1]}{letters[a][b-2]}{letters[a][b-3]}")
                    score += 1
    else:
        pass

def check_right(a, b):
    if b <= cols - 4:
        global score
        if letters[a][b+1] == "M":
            if letters[a][b+2] == "A":
                if letters[a][b+3] == "S":
                    # print(f"{letters[a][b]}{letters[a][b+1]}{letters[a][b+2]}{letters[a][b+3]}")
                    score += 1
    else:
        pass

def check_down_left(a, b):
    if a <= rows - 4 and b >= 3:
        global score
        if letters[a+1][b-1] == "M":
            if letters[a+2][b-2] == "A":
                if letters[a+3][b-3] == "S":
                    # print(f"{letters[a][b]}{letters[a+1][b-1]}{letters[a+2][b-2]}{letters[a+3][b-3]}")
                    score += 1
    else:
        pass

def check_down_right(a, b):
    if a <= rows - 3 and b <= cols - 4:
        global score
        if letters[a+1][b+1] == "M":
            if letters[a+2][b+2] == "A":
                if letters[a+3][b+3] == "S":
                    # print(f"{letters[a][b]}{letters[a+1][b+1]}{letters[a+2][b+2]}{letters[a+3][b+3]}")
                    score += 1
    else:
        pass

def check_up_left(a, b):
    if a >= 3 and b >= 3:
        global score
        if letters[a-1][b-1] == "M":
            if letters[a-2][b-2] == "A":
                if letters[a-3][b-3] == "S":
                    # print(f"{letters[a][b]}{letters[a-1][b-1]}{letters[a-2][b-2]}{letters[a-3][b-3]}")
                    score += 1
    else:
        pass

def check_up_right(a, b):
    if a >= 3 and b <= cols - 4:
        global score
        if letters[a-1][b+1] == "M":
            if letters[a-2][b+2] == "A":
                if letters[a-3][b+3] == "S":
                    # print(f"{letters[a][b]}{letters[a-1][b+1]}{letters[a-2][b+2]}{letters[a-3][b+3]}")
                    score += 1
    else:
        pass


for x in range(rows):
    for y in range(cols):
        if letters[x][y] == "X":
            check_up(x, y)
            check_down(x, y)
            check_left(x, y)
            check_right(x, y)
            check_up_left(x, y)
            check_up_right(x, y)
            check_down_left(x, y)
            check_down_right(x, y)

print(score)

