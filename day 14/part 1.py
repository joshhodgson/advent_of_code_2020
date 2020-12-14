lines = [x for x in open("input.txt").read().split("\n")]

mem = {}
mask = ""


def process(line):
    memSlot = line.split("[")[1].split("]")[0]
    number = line.split(" ")[-1]
    number = int(number)
    numberString = "{0:0>36b}".format(number)
    newNumberString = ""
    for i in range(0, len(mask)):
        if(mask[i] == "0"):
            newNumberString = newNumberString + "0"
        if(mask[i] == "1"):
            newNumberString = newNumberString + "1"
        if(mask[i] == "X"):
            newNumberString = newNumberString + numberString[i]
    mem[memSlot] = int(newNumberString, 2)


for i in lines:
    if i.startswith("mask"):
        mask = i.split(" ")[-1]
    else:
        process(i)

print(sum([mem[i] for i in mem]))
