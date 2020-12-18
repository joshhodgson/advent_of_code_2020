import re
inp = [x for x in open("input.txt").read().split("\n")]


def basicMaths(line):
    line = line.split(" ")

    while ("+" in line):
        plusIndex = line.index("+")
        line[plusIndex-1] = str(int(line[plusIndex-1]) +
                                int(line[plusIndex+1]))
        del line[plusIndex]
        del line[plusIndex]
    if(len(line) == 1):
        return int(line[0])
    res = int(line[0])*int(line[2])
    if len(line) > 3:
        return basicMaths(str(res) + " " + " ".join(line[3:]))
    else:
        return res


def process(line):
    while("(" in line):
        brk = re.search(r'\(([^\(\)]*)\)', line)
        if(brk is not None):
            line = line.replace("("+brk[1]+")", process(brk[1]))
    return str(basicMaths(line))


print(sum([int(process(x)) for x in inp]))
