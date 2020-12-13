input = [x for x in open("input.txt").read().split("\n")]


def inverseMod(z, m):
    a = 0
    z = z % m
    while a < m:
        a = a+1
        if (a*z) % m == 1:
            return a


busses = input[1].split(",")
a = []
m = []
for i, b in enumerate(busses):
    if(b == "x"):
        continue
    a.append((int(b)-i) % int(b))
    m.append(int(b))

N = 1
for n in m:
    N = N * n


z = [int(N/n) for n in m]

y = []
for i in range(0, len(a)):
    y.append(inverseMod(z[i], m[i]))

w = []
for i in range(0, len(a)):
    w.append((y[i]*z[i]) % N)

x = 0
for i in range(0, len(a)):
    x = x + a[i]*w[i]


print(int(x % N))
