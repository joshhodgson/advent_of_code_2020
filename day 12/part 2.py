instructions = [[x[0], int(x[1:])]
                for x in open("input.txt").read().split("\n")]
ew = 0
ns = 0
wpew = 10
wpns = 1

for [instruction, distance] in instructions:
    if instruction == "F":
        ew = ew + distance * wpew
        ns = ns + distance * wpns
    elif instruction == "N":
        wpns = wpns + distance
    elif instruction == "S":
        wpns = wpns - distance
    elif instruction == "E":
        wpew = wpew + distance
    elif instruction == "W":
        wpew = wpew - distance
    else:
        if instruction == "L":
            angle = (0-int(distance/90)) % 4
        elif instruction == "R":
            angle = (int(distance / 90)) % 4
        while(angle > 0):
            [wpew, wpns] = [wpns, -wpew]
            angle = angle - 1

print(abs(ew) + abs(ns))
