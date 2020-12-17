inp = [[x for x in open("input.txt").read().split("\n")]]
import copy



def countNeighbours(x, y, z):
    count = 0
    for xa in [x-1, x, x+1]:
        for ya in [y-1, y, y+1]:
            for za in [z-1, z, z+1]:
                if (ya == y and xa == x and za == z) or xa < 0 or ya < 0 or za < 0 or xa >= len(inp[0][0]) or ya >= len(inp[0]) or za >= len(inp):
                    continue
                if(inp[za][ya][xa] == "#"):
                    count = count+1
    return count

def expand():
    print(inp)
    targetX = len(inp[0][0])+2
    targetY = len(inp[0])+2
    for z in range(len(inp)):
        for y in range(len(inp[z])):
            inp[z][y] = "."+inp[z][y]+"."
        inp[z].append("."*targetX)
        inp[z].insert(0,"."*targetX)
    inp.append(["."*targetX]*targetY)
    inp.insert(0,["."*targetX]*targetY)


def printer():
    print()
    print("-----------")
    print()
    for z in inp:
        print()
        for y in z:
            print(y)
    print()
    print("-----------")
    print()

def replaceInStr(inputter,i,changeTo):
    outString = ""
    for j in range(len(inputter)):
        if j==i:
            outString = outString + changeTo
        else:
            outString = outString + inputter[j]
    return outString


cycles=6


    
for c in range(cycles):
    expand()
    newArray=copy.deepcopy(inp)
    for x in range(len(inp[0][0])):
        for y in range(len(inp[0])):
            for z in range(len(inp)):
                #print(x)
                #print(y)
                #print(z)
                th = countNeighbours(x, y, z)
                
  
                if inp[z][y][x]=="#":
                    if(th not in [2,3]):
                        newArray[z][y]=replaceInStr(newArray[z][y],x,".")
                else:
                    if th==3:
                        newArray[z][y]=replaceInStr(newArray[z][y],x,"#")
    inp = newArray


printer()
total=0
for z in inp:
    for y in z:
        total = total + y.count("#")
print(total)