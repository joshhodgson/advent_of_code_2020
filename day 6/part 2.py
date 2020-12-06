import string

groups = open("input.txt").read().split("\n\n")

def process(group):
    individuals=group.split("\n")
    groupsize=len(individuals)
    answers = [l for l in string.ascii_lowercase if ( l in group ) and ( len( [i for i in individuals if l in i] ) == groupsize ) ] ##if the letter appears and the number of individuals who answered it is the same as the number of individuals
    return len(answers)

count=0
for group in groups:
    count = count + process(group)
print(count)