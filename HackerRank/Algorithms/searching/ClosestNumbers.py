#import random
#numItems = random.randint(10, 200000)
#array = random.sample(range(-10**7,10**7),numItems)

#numItems = 10
#array = [ -20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854 ]

#numItems = 12
#array = [ -20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470 ]

#numItems = 4
#array = [ 5, 4, 3, 2, ]

numItems = int(input())
array = [ int(x) for x in input().split() ]
ans=''
assert 10 <= numItems <= 200000
assert len(array) == numItems
array.sort()
minDiff = abs(array[0] - array[1])
for i in range(len(array)-1):
    diff = abs(array[i] - array[i + 1])
    #print("minDiff=",minDiff, "i=",i, "diff=",diff)
    if diff < minDiff:
        minDiff = diff
for i in range(len(array)-1):
    diff= abs(array[i] - array[i + 1])
    if diff == minDiff:
        ans += str(array[i]) + ' ' + str(array[i+1]) + ' '
print(ans.strip())