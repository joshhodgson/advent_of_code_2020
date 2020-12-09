lines = [int(x) for x in open("input.txt").read().split("\n")]
lookBack = 25
target = 0


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
        target = num
        break

print(target)


for i, num in enumerate(lines):
    if num == target:
        continue
    for j in range(i, len(lines)+1):
        currentSum = sum(lines[i:j])
        if(currentSum > target):
            break
        elif currentSum == target:
            print(min(lines[i:j]) + max(lines[i:j]))
            break
