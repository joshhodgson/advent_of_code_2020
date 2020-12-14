lines = [x for x in open("input.txt").read().split("\n")]

mem = {}
mask = ""


def process(line):
    memSlot = line.split("[")[1].split("]")[0]
    number = int(line.split(" ")[-1])
    numberString = "{0:0>36b}".format(int(memSlot))
    newNumberString = ""
    for i in range(0, len(mask)):
        if(mask[i] == "0"):
            newNumberString = newNumberString + numberString[i]
        elif(mask[i] == "1"):
            newNumberString = newNumberString + "1"
        elif(mask[i] == "X"):
            newNumberString = newNumberString + "X"
    writer(newNumberString, number)


def writer(add, value):
    if(add.count("X") == 0):
        mem[str(int(add, 2))] = value
    else:
        writer(add.replace("X", "1", 1), value)
        writer(add.replace("X", "0", 1), value)


for i in lines:
    if i.startswith("mask"):
        mask = i.split(" ")[-1]
    else:
        process(i)


print(sum([mem[i] for i in mem]))
