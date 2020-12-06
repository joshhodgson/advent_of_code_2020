import string

groups = open("input.txt").read().split("\n\n")

def process(group):
    group.replace("\n", "")
    answers = [l for l in string.ascii_lowercase if l in group] #go through the alphabet and count how many letters have appeared
    return len(answers)

count=0
for group in groups:
    count = count + process(group)
print(count)