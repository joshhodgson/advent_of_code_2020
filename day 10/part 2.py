lines = [int(x) for x in open("input.txt").read().split("\n")]
lines = [max(lines+3), 0] + lines
lines.sort(reverse=True)
cases = [0]*len(lines)
cases[0] = 1


def process(i, n):
    if cases[i]:
        return
    runningTotal = 0
    for j, m in enumerate(lines):
        if m > n and m <= n+3:
            runningTotal = runningTotal + cases[j]
    cases[i] = runningTotal


for i, n in enumerate(lines):
    process(i, n)

print(cases[-1])
