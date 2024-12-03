import copy

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


def check_report(report):
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

    return increasing ^ decreasing



for report in reports:

    if check_report(report):
        score += 1
    else:
        for i in range(len(report)):
            report_copy = copy.deepcopy(report)
            report_copy.pop(i)
            if check_report(report_copy):
                score += 1
                break


print(score)
        