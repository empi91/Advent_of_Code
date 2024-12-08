import re

operations = []
score = 0

with open("puzzle_input") as file:
    for line in file:
        operations.append([int(x) for x in re.split(": | ", line)])


for op in operations:
    result = op[0]
    queue = []

    for i in range(1, len(op)):
        if not queue: 
            queue.append(op[i])
        else:
            q1 = []
            for value in queue:
                temp = value

                q1.append(int(str(temp) + str(op[i])))
                q1.append(temp + op[i])
                q1.append(temp * op[i])

            queue.clear()

            for item in q1:
                if item <= result:
                    queue.append(item)

        
    if result in queue: 
        score += result

print(score)