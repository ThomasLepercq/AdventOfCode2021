# Part 1
with open("./Day2/input.txt") as f:
    data = f.read().splitlines()
    X,Y = 0,0
    for line in data:
        if line.startswith("forward"):
            X += int(line[-1])
        elif line.startswith("down"):
            Y += int(line[-1])
        else:
            Y -= int(line[-1])
    print("Part 1 :", X*Y)

# Part 2 : Z becomes the aim
with open("./Day2/input.txt") as f:
    data = f.read().splitlines()
    X,Y,Z = 0,0,0
    for line in data:
        if line.startswith("forward"):
            X += int(line[-1])
            if Z:
                Y += Z*int(line[-1])
        elif line.startswith("down"):
            Z += int(line[-1])
        else:
            Z -= int(line[-1])
    print("Part 2 :", X*Y)