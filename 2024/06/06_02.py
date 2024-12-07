import copy 

area = []
score = 0

file = open("puzzle_input")

for line in file:
    area.append(list(line.strip()))

for i in range(len(area)):
    for j in range(len(area[0])):
        if area[i][j] == '^':
            starting_position = (i, j)


def count_route(area, current_position, mode):
    leave = False
    course = 'up'
    visited_positions = []

    while not leave:
        if mode: 
            area[current_position[0]][current_position[1]] = "X"

        visited_positions.append((current_position[0], current_position[1], course))
        
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

        if not mode and not leave:
            if (current_position[0], current_position[1], course) in visited_positions:
                return True


def check_obs(start_position, w_area, obstacle_postion):
    if (obstacle_postion[0], obstacle_postion[1]) != start_position: 
        w_area[obstacle_postion[0]][obstacle_postion[1]] = '#'
        return count_route(w_area, [start_position[0], starting_position[1]], 0)



count_route(area, [starting_position[0], starting_position[1]], 1)


for x, line in enumerate(area):
    for y, field in enumerate(line):
        if field == "X": 
            pos = [x, y]
            working_area = copy.deepcopy(area)
            if check_obs(starting_position, working_area, pos): score += 1



print(score)
