import numpy as np
import re
from collections import defaultdict

machines = defaultdict(list)
counter = 0
results = []
score = 0
checker = 0

with open("puzzle_input") as file:
    for line in file:
        if line.startswith("Button A"):
            a = re.search(r'X\+\d*', line.strip())[0]
            b = re.search(r'Y\+\d*', line.strip())[0]
            machines[counter] = [(int(a[2:]), int(b[2:]))]
        elif line.startswith("Button B"):
            a = re.search(r'X\+\d*', line.strip())[0]
            b = re.search(r'Y\+\d*', line.strip())[0]
            machines[counter].append((int(a[2:]), int(b[2:])))
        elif line.startswith("Prize"):
            a = re.search(r'X\=\d*', line.strip())[0]
            b = re.search(r'Y\=\d*', line.strip())[0]
            machines[counter].append((int(a[2:]) + 10000000000000, int(b[2:]) + 10000000000000))
        elif line.isspace(): counter += 1


for count, machine in enumerate(machines):
    W = np.array([[machines[machine][0][0], machines[machine][1][0]], [machines[machine][0][1], machines[machine][1][1]]])
    Wx = np.array([[machines[machine][2][0], machines[machine][1][0]], [machines[machine][2][1], machines[machine][1][1]]])
    Wy = np.array([[machines[machine][0][0], machines[machine][2][0]], [machines[machine][0][1], machines[machine][2][1]]])

    det_W = machines[machine][0][0] * machines[machine][1][1] - machines[machine][1][0] * machines[machine][0][1]
    det_Wx = machines[machine][2][0] * machines[machine][1][1] - machines[machine][1][0] * machines[machine][2][1]
    det_Wy = machines[machine][0][0] * machines[machine][2][1] - machines[machine][2][0] * machines[machine][0][1]

    x = det_Wx / det_W
    y = det_Wy / det_W

    if x%1 == 0 and y%1 == 0:
        results.append((int(x), int(y)))


for pair in results:
    score += pair[0] * 3
    score += pair[1]

print(int(score))