from math import floor, ceil
lines = [f.strip("\n") for f in open("input.txt")]

def process(line):


    low = 0
    high = 127
    mid = ((high - low ) / 2) + low
    for r in [0,1,2,3,4,5]:
        if (line[r] == "B"):
            low = ceil(mid)
        else:
            high = floor(mid)
        mid = ((high - low) / 2) + low

    if (line[6] == "B"):
        row = high
    else:
        row = low
    #print(row)
    low = 0
    high = 7
    mid = ((high - low) / 2) + low
    for r in [7,8]:
        if (line[r] == "R"):
            low = ceil(mid)
        else:
            high = floor(mid)
        mid = ((high - low) / 2) + low

    if (line[9] == "R"):
        col = high
    else:
        col = low
    #print(col)
    return(row*8+col)

    
highest = 0
idlist=[]
for l in lines:
    idn = process(l)
    idlist.append(idn)
    if (idn > highest):
        highest = idn
idlist.sort()
print(idlist)
for n in range(1,highest):
    if (n not in idlist):
        if (n - 1 in idlist) and n + 1 in idlist:
            print(n)
        

