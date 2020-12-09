lines = [int(x) for x in open("input.txt").read().split("\n")]
lookBack = 25


def match(inputArray, targetNumber):
    for i in inputArray:
        for j in inputArray:
            if i == j:
                continue
            if i+j == targetNumber:
                return True


for i, num in enumerate(lines):
    if(i < lookBack):
        continue
    if not match(lines[i-lookBack:i], num):
        print(num)
        break
