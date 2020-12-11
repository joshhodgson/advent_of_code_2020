import copy


lines = [list(x) for x in open("input.txt").read().split("\n")]


def adjOccupied(i, j):
    toCheck = []
    for y in [i-1, i, i+1]:
        if(y < 0 or y >= len(lines)):
            continue
        for x in [j-1, j, j+1]:
            if(x < 0 or x >= len(lines[0])):
                continue
            if(y == i and j == x):
                continue
            toCheck.append([y, x])
    occupied = 0
    for c in toCheck:
        if lines[c[0]][c[1]] == "#":
            occupied = occupied+1
    return occupied


def compareArrays(a, b):
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])):
            if(a[i][j] != b[i][j]):
                return False
    return True


def process():
    newlines = copy.deepcopy(lines)
    for i, r in enumerate(lines):
        for j, s in enumerate(r):
            newlines[i][j] = s
            if(s not in ["L", "#"]):
                continue
            occupied = adjOccupied(i, j)
            if(occupied == 0 and s == "L"):
                newlines[i][j] = "#"
            elif (occupied >= 4 and s == "#"):
                newlines[i][j] = "L"

    return newlines


while(True):
    newlines = process()
    if (compareArrays(lines, newlines)):
        break
    else:
        lines = newlines

print(sum([x.count("#") for x in lines]))
