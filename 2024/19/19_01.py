from functools import cache
patterns = []
score = 0
with open("puzzle_input") as file:
    for count, line in enumerate(file):
        if count == 0: towels = line.strip().split(', ')
        else:
            if not line.isspace(): patterns.append(line.strip())

@cache
def check_pattern(patts):
    poss_patterns = []
    for towel in towels:
        if patts.startswith(towel):
            if patts[len(towel):] == '': 
                return 1
            else:
                poss_patterns.append(patts[len(towel):])


    if len(poss_patterns) > 0: 
        for patt in poss_patterns: 
            if check_pattern(patt): return 1
    
    return 0

    

for pattern in patterns: 
    score += check_pattern(pattern)


print(score)