input = [int(x) for x in open("input.txt").read().split(",")]


print(input)

def list_rindex(li, x):
    newli = li[:-1]
    for i in reversed(range(len(newli))):
        if newli[i] == x:
            return i
    raise ValueError("{} is not in list".format(x))

def process():
    if input.count(input[-1])==1:
        input.append(0)
    else:
        input.append(len(input)-(list_rindex(input,input[-1])+1))


while len(input)<=2021:
    process()
print(input)
print(input[2019])