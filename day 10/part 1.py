lines = [int(x) for x in open("input.txt").read().split("\n")]

deviceJoltage=max(lines)+3

previousJoltage=0
jump1=0
jump3=1

while(True):
    if(previousJoltage==max(lines)):
        break
    
    availableChargers = [x for x in lines if x>previousJoltage and x<=previousJoltage+3]
    print(previousJoltage)
    print(availableChargers)
    if(min(availableChargers)==previousJoltage+1):
        previousJoltage=previousJoltage+1
        jump1=jump1+1
        continue
    if(min(availableChargers)==previousJoltage+3):
        previousJoltage=previousJoltage+3
        jump3=jump3+1
        continue
    print("Uh oh")
    break
print(jump1)
print(jump3)
print(jump1*jump3)