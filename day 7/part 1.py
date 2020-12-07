import re
rules = open("input.txt").read().split("\n")

containsGold=["shiny gold"]

def process():
    notchanged=False
    for i in rules:
        splitted=i.split(" bags contain ")
        if splitted[1]=="no other bags.":
            print(splitted[0] + " no other bags")
            continue
        if splitted[0] not in containsGold:
            for h in containsGold:
                if(h in splitted[1]):
                    print(splitted[0] + " contains gold")
                    containsGold.append(splitted[0])
                    notchanged=True
                    break
    return notchanged
   


while(process()):
    print("working")

print(len(containsGold)-1)
    