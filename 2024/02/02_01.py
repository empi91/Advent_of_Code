reports = []
score = 0
with open('puzzle_input') as file:
    for line in file:
        raport = []
        line = line.strip()
        line = line.split(' ')
        for num in line:
            raport.append(int(num))

        reports.append(raport)

for report in reports:
    decreasing = False
    increasing = False
    
    for index in range(1, len(report)):
        if (report[index] > report[index-1]) and (report[index] - report[index-1] <= 3):
            increasing = True
        elif (report[index] < report[index-1]) and (report[index-1] - report[index] <= 3):
            decreasing = True
        else:
            increasing = True
            decreasing = True


    if increasing ^ decreasing:
        score += 1

print(score)
        