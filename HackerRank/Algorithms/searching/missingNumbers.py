#import random
#numItems = random.randint(10, 200000)
#array = random.sample(range(-10**7,10**7),numItems)


#numA = int(input())
#arrayA = [ int(x) for x in input().split() ]
#numB = int(input())
#arrayB = [ int(x) for x in input().split() ]

#numA = 10
#arrayA = [203, 204, 205, 206, 207, 208, 203, 204, 205, 206]
#numB = 13
#arrayB = [203, 204, 204, 205, 206, 207, 205, 208, 203, 206, 205, 206, 204]
#expected output = 204 205 206

with open('test3.txt', 'r') as f:
    numA = int(f.readline())
    arrayA = [int(x) for x in f.readline().split()]
    numB = int(f.readline())
    arrayB = [int(x) for x in f.readline().split()]

#expected output = 2437 2438 2442 2444 2447 2451 2457 2458 2466 2473 2479 2483 2488 2489 2510 2515 2517 2518

ans=''
diff=[]
dictA = {}
dictB = {}

for i in arrayA:
    if i not in dictA:
        dictA[i] = 1
    else:
        dictA[i] += 1
#print ("dictA=",dictA)
for i in arrayB:
    if i not in dictB:
        dictB[i] = 1
    else:
        dictB[i] += 1
#print("dictB=",dictB)
for i in dictB:
    if i not in dictA and i not in diff:
        print("appending",i,"due to nonexistence")
        diff.append(i)
    elif dictB[i] != dictA[i] and i not in diff:
        print("appending",i,"due to inequality")
        diff.append(i)
print (" ".join([str(x) for x in diff]).strip() )

print(dictA[2419], "?=", dictB[2419])