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
    # return True
    byr = re.search(r"byr:(\d{4}) ", p)
    if(byr is not None):
        print(byr[1])
        if(int(byr[1]) < 1920) or (int(byr[1]) > 2002):
            return False
    else:
        return False

    iyr = re.search(r"iyr:(\d{4}) ", p)
    if(iyr is not None):
        print(iyr[1])
        if(int(iyr[1]) < 2010) or (int(iyr[1]) > 2020):
            return False
    else:
        return False

    eyr = re.search(r"eyr:(\d{4}) ", p)
    if(eyr is not None):
        print(eyr[1])
        if(int(eyr[1]) < 2020) or (int(eyr[1]) > 2030):
            return False
    else:
        return False

    hgt = re.search(r"hgt:(\d+)(cm|in) ", p)
    if(hgt is not None):
        print(hgt[1]+hgt[2])
        if hgt[2] == "cm" and ((int(hgt[1]) < 150) or (int(hgt[1]) > 193)):
            return False
        if hgt[2] == "in" and ((int(hgt[1]) < 59) or (int(hgt[1]) > 76)):
            return False
    else:
        return False

    hcl = re.search(r"hcl:#([0-9a-f]{6}) ", p)
    if(hcl is not None):
        print(hcl[1])
    else:
        return False

    ecl = re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth) ", p)
    if(ecl is not None):
        print(ecl[1])
    else:
        return False

    pid = re.search(r"pid:(\d{9}) ", p)
    if(pid is not None):
        print(pid[1])
    else:
        return False

    #cid=re.search(r"cid:(\d+)", p)
    # if(cid is not None):
    #    print(cid[1])

    # if any(thing+":" not in p for thing in requirements):
     #   print("Nope!")

    return True


count = 0
for p in passports:
    if(process(p)):
        count = count+1
    else:
        print("nope")


print(count)
