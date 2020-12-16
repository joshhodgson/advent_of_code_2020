input = [x for x in open("input.txt").read().split("\n\n")]

rules = input[0].split("\n")
ticket = input[1].split("\n")[1]
nearbytickets = input[2].split("\n")[1:]



ruleDict={}
for r in rules:
    ruleName = r.split(":")[0]
    ranges = r.split(": ")[1].split(" or ")
    acceptableNumbers = []
    for p in ranges:
        acceptableNumbers = acceptableNumbers + [i for i in range(int(p.split("-")[0]),int(p.split("-")[1])+1) ]
    ruleDict[ruleName]=acceptableNumbers

allValues = []
for r in ruleDict:
    allValues = list(set(allValues) | set(ruleDict[r]))

total=0
for t in nearbytickets:
    values = [int(v) for v in t.split(",") if int(v) not in allValues]
    total = total + sum(values)

print(total)