import numpy as np

# Returns most common number (1 or 0) on the pos-th column
def mostCommon(arr,pos):
    total = len(arr)
    ones = arr.sum(axis=0)
    return  int(ones[pos] >= total/2)

with open("./Day3/input.txt") as f:
    data = f.read().splitlines()
    arr = []
    for line in data:
        arr.append(list(map(int,list(line))))
    arr = np.asarray(arr)

    # Part 1
    length = len(arr)
    gamma = ""
    ones = arr.sum(axis=0)
    for i in range(len(ones)):
        gamma += str(mostCommon(arr,i))
    
    epsilon = int("0b"+gamma,2)^0b111111111111 # XOR trick to avoid using array again
    print("Part 1 :",int("0b"+gamma,2)*epsilon)

    # Part 2
    copy = arr.copy()
    for i in range(len(ones)):
        # O2 selection
        most = mostCommon(arr,i)
        if len(arr) > 1:
            arr = arr[arr[:,i] == most]
        # CO2 selection
        most = mostCommon(copy,i)
        if len(copy) > 1:
            copy = copy[copy[:,i] != most]
    
    # Read resulting binaries
    oxygen = ""
    for i in range(len(arr[0])):
        oxygen += str(arr[0][i])
    carbon = ""
    for i in range(len(copy[0])):
        carbon += str(copy[0][i])
    print("Part 2 :",int("0b"+oxygen,2)*int("0b"+carbon,2))