inp = [x for x in open("input.txt").read().split("\n\n")]
ruleInp = inp[0].split("\n")
matchInp = inp[1].split("\n")

rules = {}


def gene(inpRules):
    ruleNumbers = m.split(" ")
    options = rules[ruleNumbers[0]]
    newoptions = []
    for r in ruleNumbers[1:]:
        for p in rules[r]:
            for o in options:
                newoptions.append(o + p)
        options = newoptions
        newoptions = []
    return options


complete = False
while not complete:
    complete = True
    for i in ruleInp:
        if i.split(": ")[0] in rules:
            continue
        complete = False
        if '"' in i:
            rules[i.split(": ")[0]] = [i.split(" ")[1].replace('"', '')]
            continue
        toMatch = i.split(": ")[1].split(" | ")
        if all(n in rules for n in i.split(": ")[1].replace(" | ", " ").split(" ")):
            rules[i.split(": ")[0]] = []
            for m in toMatch:
                rules[i.split(": ")[0]] = rules[i.split(": ")[0]] + gene(m)


print(len([i for i in matchInp if i in rules["0"]]))
