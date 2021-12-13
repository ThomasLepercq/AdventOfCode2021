import numpy as np

def lowPoint(data,i,j):
    if i == 0 or j == 0 or i == x - 1 or j == y - 1:
        neighbours = []
        if i != 0:
            neighbours.append(data[i - 1][j])
        if j != 0:
            neighbours.append(data[i][j - 1])
        if i != x - 1:
            neighbours.append(data[i + 1][j])
        if j != y - 1:
            neighbours.append(data[i][j + 1])
        if data[i][j] < min(neighbours):
            return True
    elif data[i][j] < min(data[i-1][j],data[i][j-1],data[i+1][j],data[i][j+1]):
            return True
    return False

with open("./Day9/input.txt") as f:
    data = f.read().splitlines()
    for i, line in enumerate(data):
        data[i] = list(map(int, line))
    data = np.asarray(data)

    # Part 1
    risk = 0
    x, y = data.shape[0], data.shape[1]
    for i in range(x):
        for j in range(y):
            if lowPoint(data,i,j):
                risk += data[i][j] + 1
    print("Part 1 :", risk)

    # Part 2