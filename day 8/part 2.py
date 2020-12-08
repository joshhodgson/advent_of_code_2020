lines = open("input.txt").read().split("\n")


def process(newlist):
    acc = 0
    i = 0
    runInstruction = []
    while i not in runInstruction:
        runInstruction.append(i)
        if(i == len(newlist)):
            print(acc)
            return True
        l = newlist[i]
        if l.startswith("nop"):
            i = i+1
            continue
        if l.startswith("acc"):
            acc = acc + int(l.split(" ")[1])
            i = i+1
            continue
        if l.startswith("jmp"):
            i = i + int(l.split(" ")[1])
            continue


for n, l in enumerate(lines):
    newlist = lines.copy()
    if(l.startswith("nop")):
        newlist[n] = l.replace("nop", "jmp")
        if(process(newlist)):
            break
    if(l.startswith("jmp")):
        newlist[n] = l.replace("jmp", "nop")
        if(process(newlist)):
            break
