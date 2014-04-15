#import random

#numIntegers = random.randrange(1,100,2)
#intArray = random.sample(range(0,100),numIntegers)
#numIntegers=1
#intArray=[1]
#output 1

#numIntegers=3
#intArray=[1, 1, 2]
##output 2

#numIntegers=5
#intArray=[0, 0, 1, 2, 1]

#should be linear? depends on what append and remove do...



numIntegers = int(input())
intArray = [ int(x) for x in input().split() ]

assert 1 <= numIntegers <= 100
assert numIntegers % 2 == 1 #numIntegers needs to be odd
assert len(intArray) == numIntegers

once=[]
twice=[]

for x in intArray: #0n
    if x in once:
        twice.append(x)
        once.remove(x)
    else:
        once.append(x)
print(once[0])
