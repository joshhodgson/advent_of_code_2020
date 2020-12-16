input = [int(x) for x in open("input.txt").read().split(",")]


lastOccurance = dict()
targetN = 30000000
#targetN = 2020
lastNumber = None

for i in range(len(input)-1):
    lastOccurance[input[i]] = i

currentIndex = len(input)
lastNumber = input[-1]

while currentIndex < targetN:
    if(lastNumber not in lastOccurance):  # first time
        lastOccurance[lastNumber] = currentIndex-1
        lastNumber = 0
    else:
        newNumber = currentIndex - lastOccurance[lastNumber]-1
        lastOccurance[lastNumber] = currentIndex-1
        lastNumber = newNumber
    currentIndex = currentIndex + 1


print(lastNumber)
