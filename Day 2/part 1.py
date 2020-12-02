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
    if not (passwd.count(letter)>=minc and passwd.count(letter)<=maxc):
        #print("Got a bad one!")
        return False
    else:
        return True

counter=0
for i in lines:
    if(process(i)):
        counter = counter+1
print(counter)