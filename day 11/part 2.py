import copy


lines = [list(x) for x in open("input.txt").read().split("\n")]


def adjOccupied(i, j):
    occupied = 0
    for y in [1, 0, -1]:
        for x in [1, 0, -1]:
            if y == 0 and x == 0:
                continue
            currenty = i + y
            currentx = j + x
            while currentx >= 0 and currentx < len(lines[0]) and currenty >= 0 and currenty < len(lines):
                if lines[currenty][currentx] == "#":
                    occupied = occupied + 1
                    break
                elif lines[currenty][currentx] == "L":
                    break
                currentx = x + currentx
                currenty = y + currenty
    return occupied


def differentArrays(a, b):
    for i in range(0, len(lines)):
        for j in range(0, len(lines[0])):
            if a[i][j] != b[i][j]:
                return True


def process():
    newlines = copy.deepcopy(lines)
    for i, r in enumerate(lines):
        for j, s in enumerate(r):
            newlines[i][j] = s
            if s not in ["L", "#"]:
                continue
            occupied = adjOccupied(i, j)
            if occupied == 0 and s == "L":
                newlines[i][j] = "#"
            elif occupied >= 5 and s == "#":
                newlines[i][j] = "L"
    return newlines


while(True):
    newlines = process()
    if not differentArrays(lines, newlines):
        break
    else:
        lines = newlines


print(sum([x.count("#") for x in lines]))
