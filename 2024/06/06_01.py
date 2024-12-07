area = []
leave = False
score = 0

file = open("puzzle_input")

for line in file:
    area.append(list(line.strip()))

for i in range(len(area)):
    for j in range(len(area[0])):
        if area[i][j] == '^':
            current_position = [i, j]

course = 'up'

while not leave:
    area[current_position[0]][current_position[1]] = "X"
    if course == 'up':
        if current_position[0] == 0: leave = True
        else:
            if area[current_position[0] - 1][current_position[1]] == "#":
                course = "right"
            else:
                current_position[0] -= 1

    elif course == 'right':
        if current_position[1] == len(area[0]) - 1: leave = True
        else:
            if area[current_position[0]][current_position[1] + 1] == "#":
                course = 'down'
            else:
                current_position[1] += 1

    elif course == 'down':
        if current_position[0] == len(area) - 1: leave = True
        else:
            if area[current_position[0] + 1][current_position[1]] == "#":
                course = 'left'
            else:
                current_position[0] += 1

    elif course == 'left':
        if current_position[1] == 0: leave = True
        else:
            if area[current_position[0]][current_position[1] - 1] == "#":
                course = 'up'
            else:
                current_position[1] -= 1
 



for line in area:
    print(line)
    for field in line:
        if field == "X": score += 1


print(score)
