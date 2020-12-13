input = [x for x in open("input.txt").read().split("\n")]

timestamp = int(input[0])
busses = input[1].split(",")

currentTime = timestamp
notFound = True
while notFound:
    for b in busses:
        if b == "x":
            continue
        if timestamp % int(b) == 0:
            print(int(b)*(timestamp-currentTime))
            notFound = False
    timestamp = timestamp + 1
