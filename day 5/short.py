seats = [(int(l[0:7].replace("B", "1").replace("F", "0"), 2) * 8 + int(l[7:12].replace("L", "0").replace("R", "1"), 2)) for l in open("input.txt")]


print("Part 1: ")
print(max(seats))

print("Part 2: ")
print([j+1 for j in seats if (j+1 not in seats and j+2 in seats)][0])
