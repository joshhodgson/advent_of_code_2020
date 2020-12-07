import re
rules = open("input.txt").read().split("\n")

containsGold=["shiny gold"]
noOtherBags=[]
bags={}

def process():
    notchanged=False
    for i in rules:
        splitted=i.split(" bags contain ")
        if splitted[1]=="no other bags.":
            if splitted[1] not in noOtherBags:
                noOtherBags.append(splitted[0]+" bags")
            continue
        if splitted[0] not in containsGold:
            for h in containsGold:
                if(h in splitted[1]):
                    containsGold.append(splitted[0])
                    notchanged=True
                    break
    return notchanged
   


while(process()):
    process()

print(len(containsGold)-1)




def count(c): ##input [n, colour]
    if c[1] in noOtherBags:
        return int(c[0])
    c[0]=int(c[0])
    n = c[0]
    innerbag=[ b for b in rules if b.startswith(c[1])][0].replace(".","").split( " contain ")[1].split(", ")
    if(innerbag[0]=="no other bags"):
        return n
    for i in innerbag:
        n = n + c[0] * count(i.split(" ",1))
    return(n)
print(count([1, "shiny gold"])-1)
