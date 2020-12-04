import os
import time
import re
filepointer = open("input.txt")
contents = filepointer.read()
# print(contents)
passports = contents.split("\n\n")

requirements = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]  # , "cid"]


def process(p):
    p = p.replace("\n", " ") + " "
    print(p)

    for thing in requirements:
        if thing+":" not in p:
            print("nope")
            return False
    return True
    


count = 0
for p in passports:
    if(process(p)):
        count = count+1
    else:
        print("nope")


print(count)
