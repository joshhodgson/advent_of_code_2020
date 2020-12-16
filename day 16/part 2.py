input = [x for x in open("input.txt").read().split("\n\n")]

rules = input[0].split("\n")
ticket = input[1].split("\n")[1].split(",")
nearbytickets = input[2].split("\n")[1:]
ruleDict = {}
columns = []


for r in rules:
    ruleName = r.split(":")[0]
    ranges = r.split(": ")[1].split(" or ")
    acceptableNumbers = []
    for p in ranges:
        acceptableNumbers = acceptableNumbers + \
            [i for i in range(int(p.split("-")[0]), int(p.split("-")[1])+1)]
    ruleDict[ruleName] = acceptableNumbers # {rule: [array of options], etc}

allValues = []
for r in ruleDict:
    allValues = list(set(allValues) | set(ruleDict[r]))

for j in range(len(ticket)):
    columns.append([r for r in ruleDict])

for t in nearbytickets:
    if(len([int(v) for v in t.split(",") if int(v) not in allValues]) > 0):  # discard invalid tickets
        continue
    for i, n in enumerate([int(v) for v in t.split(",")]):
        for r in ruleDict:
            if n not in ruleDict[r]:
                columns[i].remove(r)

while len([c for c in columns if len(c) > 1]) > 0:
    for i in range(len(columns)):
        if len(columns[i]) == 1: # if this column is defined, remove that possibility from all other columns
            r = columns[i][0]
            for j in columns:
                if(len(j) > 1) and r in j:
                    j.remove(columns[i][0])


total = 1
for i, c in enumerate(columns):
    if c[0].startswith("departure"):
        total = total * int(ticket[i])
print(total)
#[2, 14, 13, 9, 18, 17, 11, 4, 3, 5, 1, 20, 19, 7, 10, 8, 15, 16, 12, 6]
#[1, 13, 12, 8, 17, 16, 10, 3, 2, 4, 1, 19, 18, 6, 9, 7, 14, 15, 11, 5]
