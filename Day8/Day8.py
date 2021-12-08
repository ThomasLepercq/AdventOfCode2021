with open("./Day8/input.txt") as f:
    data = f.read().splitlines()

    # Part 1 : Count "simple" digits
    count = 0
    for line in data:
        l,r = line.split(" | ")
        r = r.split(" ")
        count += sum(len(x) in [2,3,4,7] for x in r)
    print("Part 1 :", count)

    # Part 2 : Count sum of all displayed numbers
    # This part definitely could use some optimization, but it's not too computationnally
    # nor memory expensive anyway so it's fine for today
    count = 0

    for line in data:
        l,r = line.split(" | ")
        l,r = l.split(" "),r.split(" ")

        # Map all combinations for the 7-segment display
        # 'a' is match[0], 'b' is match[1], ... up to 'g'
        match = [{"a","b","c","d","e","f","g"} for i in range(7)] 
        for number in l:
            number = set(number)
            if len(number) == 2: # 1 is displayed with "c" and "f"
                match[2] = number & match[2] # Set intersection
                match[5] = number & match[5]
            elif len(number) == 3: # 7 is displayed with "a", "c" and "f"
                match[0] = number & match[0]
                match[2] = number & match[2]
                match[5] = number & match[5]
            elif len(number) == 4: # 4 is displayed with "b", "c", "d" and "f"
                match[1] = number & match[1]
                match[2] = number & match[2]
                match[3] = number & match[3]
                match[5] = number & match[5]
            elif len(number) == 5: # 2, 3 and 5 have "a", "d" and "g" as common display outputs
                match[0] = number & match[0]
                match[3] = number & match[3]
                match[6] = number & match[6]
            elif len(number) == 6: # 0, 6 and 9 have "a", "b", "f" and "g" as common display outputs
                match[0] = number & match[0]
                match[1] = number & match[1]
                match[5] = number & match[5]
                match[6] = number & match[6]

        # Final match cleaning
        match[1] = match[1] - match[5]
        match[2] = match[2] - match[5]
        match[6] = match[6] - match[0]
        match[4] = match[4] - set.union(match[0], match[1], match[2], match[3], match[5], match[6])
        
        # Read actual display
        match = [match[i].pop() for i in range(len(match))]
        display = ""

        for number in r:
            if len(number) == 2:
                display += "1"
            elif len(number) == 3:
                display += "7"
            elif len(number) == 4:
                display += "4"
            elif len(number) == 5: # 2, 3 or 5
                if match[1] in set(number): # Only 5 has "b" lit
                    display += "5"
                elif match[4] in set(number): # Only 2 has "e" lit
                    display += "2"
                else:
                    display += "3"
            elif len(number) == 6: # 0, 6 or 9
                if match[3] not in set(number): # Only 0 does not have "d" lit
                    display += "0"
                elif match[2] not in set(number): # Only 6 does not have "c" lit
                    display += "6"
                else:
                    display += "9"
            elif len(number) == 7:
                display += "8"

        count += int(display)
    print("Part 2 :", count)