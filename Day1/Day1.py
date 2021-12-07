import numpy as np

# Part 1
with open("./Day1/input.txt") as f:
    data = list(map(int, f.read().splitlines()))
    count = 0
    top = np.inf
    for depth in data:
        if depth > top:
            count += 1
        top = depth
    print("Part 1 :", count)

# Part 1
with open("./Day1/input.txt") as f:
    data = list(map(int, f.read().splitlines()))
    count = 0
    for i in range(len(data) - 3):
        if sum(data[i+1 : i+4]) > sum(data[i : i+3]):
            count += 1
    print("Part 2 :", count)
