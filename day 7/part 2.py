rules = open("input.txt").read().split("\n")

def count(c): ##input [n, colour]
    c[0]=int(c[0])
    n = c[0]
    innerbag=[ b for b in rules if b.startswith(c[1])][0].replace(".","").split( " contain ")[1].split(", ")
    if(innerbag[0]=="no other bags"):
        return n
    for i in innerbag:
        n = n + c[0] * count(i.split(" ",1))
    return(n)
print(count([1, "shiny gold"])-1)
