import os
lines = [f.strip("\n") for f in open("input.txt")]


def process(i):
    minc = int(i.split("-")[0])
    maxc = int(i.split("-")[1].split(" ")[0])
    letter=i.split(" ")[1].split(":")[0]
    passwd=i.split(" ")[-1]
    #print(minc)
    #print(maxc)
    #print(letter)
    #print(passwd)
    if (passwd[minc-1]==letter and not passwd[maxc-1]==letter):
        #print("Got a bad one!")
        return True
    elif (not passwd[minc-1]==letter and passwd[maxc-1]==letter):
        return True
    else:
        return False

counter=0
for i in lines:
    if(process(i)):
        counter = counter+1
print(counter)