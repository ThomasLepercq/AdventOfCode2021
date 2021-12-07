import numpy as np

def dist(n):
    return int(n*(n+1)/2)

with open("./Day7/input.txt") as f:
    data = list(map(int,f.read().split(",")))

    # Part 1 : The median value splits evenly the list by "distance"
    median = int(np.median(data))
    distances = [abs(x-median) for x in data]
    print("Part 1 :", sum(distances))

    # Part 2 : The distance is not linear anymore, the average is what we need now.
    avg = int(np.average(data))
    distances = [dist(abs(x-avg)) for x in data]
    print("Part 2 :", sum(distances))