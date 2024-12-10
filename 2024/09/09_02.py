from collections import defaultdict
from collections import deque
import re
index = 0
free_spaces = 0
counter = 0
score = 0
mapping = str()
replacables = []
num_pos = {}
dot_pos = []
# empty_pos = defaultdict(list)
pos = defaultdict(list)
lpositions = deque()


with open("puzzle_input") as f:
    for line in f:
        disc = str(line)



for count, i in enumerate(disc):
    for j in range(int(i)): 
        if count % 2 == 0:
            mapping = mapping + str(index)
        else:
            mapping = mapping + '.'
    if count % 2 == 0: index += 1

print(mapping)
# lpositions = mapping


index_list = [r'(\d)\1*', r'\.+'] 
# index_list = [r'(\d)\1+'] 

for index in index_list:
    for match in re.finditer(index, mapping):
        lpositions.extend([match.group(), match.span(), match.span()[1] - match.span()[0]])
        # if not pos[match.group()]:
            # pos[match.group()] = [match.span()]
        # else:
        #     pos[match.group()].append([match.span()])


# for entry , positions in pos.items(): 
#     print(entry, positions)


# print(lpositions)
for line in lpositions:
    print(line)


# prev_char = ''
# for pos, char in enumerate(mapping):
#     if char == '.': 
#         if char != prev_char: 
#             # print(pos)
#             empty_pos[char] = [pos]
#         else:
#             # print(pos)
#             empty_pos[char].append(pos)
#     prev_char = char

# print(empty_pos)


# for j in range(len(mapping) - 1, 0, -1):
#     if counter < free_spaces:    
#         if mapping[j] != '.': 
#             replacables.append(mapping[j])
#             mapping.pop(j)
#     counter += 1


# for idx, char in enumerate(mapping):
#     if char == '.': 
#         if replacables:
#             mapping[idx] = replacables[0]
#             replacables.pop(0)


# for i in range(free_spaces):
#     mapping.append('.')


# for pos, char in enumerate(mapping):
#     if char != '.': score += pos * int(char)

# print(score)

