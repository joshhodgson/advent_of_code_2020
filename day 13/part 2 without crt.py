input = [x for x in open("input.txt").read().split("\n")]


delta = []
bussesShort = []
match = []

for i, b in enumerate(input[1].split(",")):
    if(b == "x"):
        continue
    delta.append(i)
    bussesShort.append(int(b))
    match.append(False)

jump = 1
currentTime = 0


def process():
    global jump
    global currentTime

    for i in range(0, len(bussesShort)):
        if not match[i]:
            if((currentTime + delta[i]) % bussesShort[i] == 0):
                match[i] = True
                jump = jump * bussesShort[i]
    if all(match):
        return True
    currentTime = currentTime + jump


while True:
    if(process()):
        print(currentTime)
        break
