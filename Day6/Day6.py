with open("./Day6/input.txt") as f:
    data = list(map(int,f.read().split(",")))

    # Part 1 : Naive method
    fishes = data.copy()
    for day in range(80):
        for i in range(len(fishes)):
            if fishes[i] == 0:
                fishes[i] = 6
                fishes.append(8)
            else:
                fishes[i] -= 1
    print("Part 1 :",len(fishes))

    # Part 2 : Cycling population method
    cycle = [data.count(i) for i in range(9)]
    for day in range(256):
        temp = cycle[0]
        cycle[0:8] = cycle[1:9]
        cycle[8] = temp
        cycle[6] += temp
    print("Part 2 :",sum(cycle))