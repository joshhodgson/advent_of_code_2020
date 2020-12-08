lines = open("input.txt").read().split("\n")

runInstruction = []
acc = 0
i = 0
while i not in runInstruction:
    runInstruction.append(i)
    l = lines[i]
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
print(acc)
