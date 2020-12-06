import string

groups = open("input.txt").read().split("\n\n")

pt1 = sum([len([l for l in string.ascii_lowercase if ( l in group ) ]) for group in groups])
print(pt1)
pt2 = sum([len([l for l in string.ascii_lowercase if ( l in group ) and ( len( [i for i in group.split("\n") if l in i] ) == group.count("\n")+1 ) ]) for group in groups])
print(pt2)