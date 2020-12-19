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
        if i.split(": ")[0] in rules or i.split(": ")[0] in ["0", "8", "11"]:
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

ruleInp = ["0: 8 11",
           "8: 42 | 42 8",
           "11: 42 31 | 42 11 31"]  # so (>1)*42 then n*42 and n*31


def matcher(m):
    cnt = True
    count42 = 0
    count31 = 0
    while cnt:
        cnt = False
        for o in rules["42"]:
            if m.startswith(o):
                cnt = True
                count42 = count42+1
                m = m.replace(o, "", 1)
    cnt = True
    while cnt:
        cnt = False
        for o in rules["31"]:
            if m.startswith(o):
                cnt = True
                count31 = count31+1
                m = m.replace(o, "", 1)
    if m == "" and not (count31 >= count42) and count42 > 1 and count31 > 0:
        return True
    else:
        return False


# not 417,408, too high. not 404.. 403!
print(len([m for m in matchInp if matcher(m)]))
