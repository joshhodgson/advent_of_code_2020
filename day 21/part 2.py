inp = [x for x in open("input.txt").read().split("\n")]

allergens = {}
allIngredients = []
allAllIngredients = []
actualAllergens={}
for i in inp:
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

while False:#len([a for a in allergens if len(allergens[a])>1])    >0:
    exclusives= [allergens[a][0] for a in allergens if len(allergens[a])==1]
    for e in exclusives:
        for b in [a for a in allergens if len(allergens[a])>1]:
            while(e in allergens[b]):
                allergens[b].remove(e)
    



for j in [a for a in allergens ]:
    if j not in actualAllergens:
        actualAllergens[j]=[]
    ingredientList = allergens[j]
    for k in  [x for x in set().union(*allergens[j])]:
        if all([ (k in l) for l in allergens[j]]):
            print(j + " must be in " + k)
            if k not in actualAllergens[j]:
                actualAllergens[j].append(k)
            if k in allIngredients:
                allIngredients.remove(k)

while not all([len(actualAllergens[p])==1 for p in actualAllergens]):
    for i in [o for o in actualAllergens if len(actualAllergens[o])==1]:
        for j in actualAllergens:
            if j != i:
                while(actualAllergens[i][0] in actualAllergens[j]):
                    actualAllergens[j].remove(actualAllergens[i][0])
print(actualAllergens)
out = []
for i in (sorted(actualAllergens)):
    print(actualAllergens[i][0])
    out.append(actualAllergens[i][0])
print(",".join(out))


