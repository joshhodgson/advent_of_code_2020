inp = [[[x for x in open("input.txt").read().split("\n")]]]
import copy



def countNeighbours(w, z, y, x):
    count = 0
    chk=0
    for xa in [x-1, x, x+1]:
        for ya in [y-1, y, y+1]:
            for za in [z-1, z, z+1]:
                for wa in [w-1,w,w+1]:
                    if (ya == y and xa == x and za == z and wa==w) or xa < 0 or ya < 0 or za < 0 or wa<0 or xa>=len(inp[0][0][0]) or ya >= len(inp[0][0]) or za >= len(inp[0]) or wa >= len(inp):
                        #print([wa,za,ya,xa])
                        continue
                    chk = chk+1
                    if(inp[wa][za][ya][xa] == "#"):
                        count = count+1
    return count

def expand():
    targetX = len(inp[0][0][0])+2
    targetY = len(inp[0][0])+2
    for w in range(len(inp)):
        for z in range(len(inp[w])):
            for y in range(len(inp[w][z])):
                inp[w][z][y] = "."+inp[w][z][y]+"."
            inp[w][z].append("."*targetX)
            inp[w][z].insert(0,"."*targetX)
        inp[w].append(["."*targetX]*targetY)
        inp[w].insert(0,["."*targetX]*targetY)
    inp.insert(0, copy.deepcopy(inp[0]) ) 
    inp.append(copy.deepcopy(inp[0]) )
    for j in [0,-1]:
        for z in range(len(inp[j])):
            for y in range(len(inp[j][z])):
                inp[j][z][y]="."*len(inp[j][z][y])


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
    for x in range(len(inp[0][0][0])):
        for y in range(len(inp[0][0])):
            for z in range(len(inp[0])):
                for w in range(len(inp)):
                    #print(x)
                    #print(y)
                    #print(z)
                    th = countNeighbours(w, z, y, x)
                    
    
                    if inp[w][z][y][x]=="#":
                        if(th not in [2,3]):
                            newArray[w][z][y]=replaceInStr(newArray[w][z][y],x,".")
                    else:
                        if th==3:
                            newArray[w][z][y]=replaceInStr(newArray[w][z][y],x,"#")
    inp = newArray


total=0
for w in inp:
    for z in w:
        for y in z:
            total = total + y.count("#")
print(total)