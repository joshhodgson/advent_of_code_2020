inp = [x for x in open("input.txt").read().split("\n")]

allergens = {}
allIngredients = []
allAllIngredients = []
for i in inp:
    print(i)
    ingredients = i.split(" (")[0].split(" ")
    thisAllergens = i.split("(contains ")[1].replace(")","").split(", ")
    for i in ingredients:
        if i not in allIngredients:
            allIngredients.append(i)
        allAllIngredients.append(i)
    for a in thisAllergens:
        if a not in allergens:
            allergens[a]=[]
        allergens[a].append(ingredients)
print(allergens)

while False:#len([a for a in allergens if len(allergens[a])>1])    >0:
    exclusives= [allergens[a][0] for a in allergens if len(allergens[a])==1]
    for e in exclusives:
        for b in [a for a in allergens if len(allergens[a])>1]:
            while(e in allergens[b]):
                allergens[b].remove(e)
    
    print(allergens)

def removeFromAll(v, o):
    print("removing " + v)
    for j in [k for k in allergens]:
        if j!=o:
            continue
        for i in allergens[j]:
            while v in i:
                i.remove(v)


for j in [a for a in allergens ]:
    ingredientList = allergens[j]
    for k in  [x for x in set().union(*allergens[j])]:
        if all([ (k in l) for l in allergens[j]]):
            print(j + " must be in " + k)
            if k in allIngredients:
                allIngredients.remove(k)
    allergens[j] = [[k]]
print(allergens)
print(allIngredients)
count = 0
for i in allIngredients:
    count = count + allAllIngredients.count(i)
print(count)