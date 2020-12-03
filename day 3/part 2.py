import os
lines = [f.strip("\n") for f in open("input.txt")]


def process(i, n):
    if(i[n]=="#"):
        #print("tree")
        return True
    else:
        #print("open")
        return False
total=1
counter=0
n=0
length = len(lines[0])
print(length)
for i in lines:
    if n>=length:
        n = n-length
    if(process(i, n)):
        counter = counter+1
    n = n+1
print(counter)
total=total*counter

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
total=total*counter

counter=0
n=0
length = len(lines[0])
for i in lines:
    if n>=length:
        n = n-length
    if(process(i, n)):
        counter = counter+1
    n = n+5
print(counter)
total=total*counter

counter=0
n=0
length = len(lines[0])
for i in lines:
    if n>=length:
        n = n-length
    if(process(i, n)):
        counter = counter+1
    n = n+7
print(counter)
total=total*counter

counter=0
n=0
length = len(lines[0])
skip=True
for i in lines:
    skip = not skip
    if(skip):
        continue
    if n>=length:
        n = n-length
    #print(i)
    if(process(i, n)):
        counter = counter+1
    n = n+1
print(counter)
total=total*counter

print(total)