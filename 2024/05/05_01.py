from collections import defaultdict

orders = []
pages = []
rules = defaultdict(list)
correct_pages = []
score = 0

with open("puzzle_input") as file:
    for line in file:
        if '|' in line:
            orders.append(list(map(int, line.strip().split('|'))))
        elif line.strip() != "":
            pages.append(list(map(int, line.strip().split(','))))


for o in orders:
    rules[o[0]].append(o[1])


for page in pages:
    valid = True
    for count, value in enumerate(page):
        for n in page[:count]:
            if n in rules[value]:
                valid = False
    if valid:
        correct_pages.append(page)
        

for correct in correct_pages:
    score += correct[int((len(correct)-1)/2)]

print(score)