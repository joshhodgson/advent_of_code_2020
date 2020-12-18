import re
inp = [x for x in open("input.txt").read().split("\n")]


def basicMaths(line):
    line = line.split(" ")
    n1 = line[0]
    op = line[1]
    n2 = line[2]
    if op == "*":
        res = int(n1)*int(n2)
    elif op == "+":
        res = int(n1) + int(n2)
    if len(line) > 3:
        return basicMaths(str(res) + " " + " ".join(line[3:]))
    else:
        return res


def process(line):
    #print("Processing " + line)
    while("(" in line):
        brk = re.search(r'\(([^\(\)]*)\)', line)
        if(brk is not None):
            line = line.replace("("+brk[1]+")", process(brk[1]))
    return str(basicMaths(line))


print(sum([int(process(x)) for x in inp]))
