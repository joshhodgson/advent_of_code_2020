instructions = [[x[0], int(x[1:])]
                for x in open("input.txt").read().split("\n")]
ew = 0
ns = 0
headings = [[1, 0], [0, -1], [-1, 0], [0, 1]]
heading = 0

for [instruction, distance] in instructions:
    if instruction == "F":
        ew = ew + distance * headings[heading][0]
        ns = ns + distance * headings[heading][1]
    elif instruction == "N":
        ns = ns + distance
    elif instruction == "S":
        ns = ns - distance
    elif instruction == "E":
        ew = ew + distance
    elif instruction == "W":
        ew = ew - distance
    elif instruction == "L":
        heading = (heading - int(distance/90)) % 4
    elif instruction == "R":
        heading = (heading + int(distance / 90)) % 4

print(abs(ew) + abs(ns))
