from collections import defaultdict

orders = []
pages = []
rules = defaultdict(list)
correct_pages = []
wrong_pages = []
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
    else:
        wrong_pages.append(page)


for wrong in wrong_pages:
    changed = True
    while changed:
        changed = False
        for i in range(len(wrong)):
            for n in wrong[:i]:
                if n in rules[wrong[i]]:
                    wrong.insert(i-1, wrong[i])
                    wrong.pop(i+1)
                    changed = True

for wrong in wrong_pages:
    score += wrong[int((len(wrong)-1)/2)]


print(score)