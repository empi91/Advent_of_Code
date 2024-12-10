index = 0
free_spaces = {}
counter = 0
score = 0
mapping = []
replacables = []


with open("puzzle_input") as f:
    for line in f:
        disc = str(line)


for count, i in enumerate(disc):
    for j in range(int(i)): 
        if count % 2 == 0:
            mapping.append(index)
        else:
            mapping.append('.')
    if count % 2 == 0: index += 1


for char in mapping:
    if char == '.': free_spaces += 1


for j in range(len(mapping) - 1, 0, -1):
    if counter < free_spaces:    
        if mapping[j] != '.': 
            replacables.append(mapping[j])
            mapping.pop(j)
    counter += 1


for idx, char in enumerate(mapping):
    if char == '.': 
        if replacables:
            mapping[idx] = replacables[0]
            replacables.pop(0)


for i in range(free_spaces):
    mapping.append('.')


for pos, char in enumerate(mapping):
    if char != '.': score += pos * int(char)

print(score)
        
