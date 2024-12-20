from functools import cache
patterns = []
score = 0
with open("puzzle_input") as file:
    for count, line in enumerate(file):
        if count == 0: towels = line.strip().split(', ')
        else:
            if not line.isspace(): patterns.append(line.strip())


@cache
def check_pattern(pattern):
    count  = 0
    for towel in towels:
        if pattern.startswith(towel):
            if pattern[len(towel):] == '': count += 1
            else: 
                count += check_pattern(pattern[len(towel):])

    return count


for pattern in patterns:
    score += check_pattern(pattern)

print(score)