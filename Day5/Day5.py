import numpy as np

def drawLines(lines,dim,diagonals):
    arr = np.zeros((dim+1,dim+1),int)
    for line in lines:
        # Part 1
        if line[0] == line[2]:
            down, up = min(line[1],line[3]), max(line[1],line[3])
            for i in range(down,up+1):
                arr[line[0]][i] += 1
        elif line[1] == line[3]:
            down, up = min(line[0],line[2]), max(line[0],line[2])
            for i in range(down,up+1):
                arr[i][line[1]] += 1

        # Part 2        
        elif diagonals:
            gap = abs(line[0] - line[2])
            x = 1 if line[0] < line[2] else -1
            y = 1 if line[1] < line[3] else -1
            for i in range(gap+1):
                arr[line[0] + x*i][line[1] + y*i] += 1
    return np.sum(arr >= 2)

with open("./Day5/input.txt") as f:
    data = f.read().splitlines()
    lines = []
    dim = -1
    for line in data:
        l,r = line.split(" -> ")
        ll,lr = l.split(",")
        rl,rr = r.split(",")
        newLine = [int(ll),int(lr),int(rl),int(rr)]
        lines.append(newLine)
        if dim < max(newLine):
            dim = max(newLine)
    
    print("Part 1 :",drawLines(lines,dim,False))
    print("Part 2 :",drawLines(lines,dim,True))
