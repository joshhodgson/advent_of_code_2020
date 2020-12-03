import os
lines = [f.strip("\n") for f in open("input.txt")]


def process(i, n):
    if(i[n]=="#"):
        print("tree")
        return True
    else:
        print("open")
        return False

counter=0
n=0
length = len(lines[0])
for i in lines:
    if n>=length:
        n = n-length
    if(process(i, n)):
        counter = counter+1
    n = n+3
print(counter)