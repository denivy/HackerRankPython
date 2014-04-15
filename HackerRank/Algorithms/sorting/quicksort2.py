numItems=int(input())
assert 1 <= numItems <= 1000
array=[int(x) for x in input().split(' ')]
p=array[0]
array.pop(0)
head=[]
tail=[]
for i in array:
    if p < i:
        tail.append(i)
    if p > i:
        head.append(i)
sortz = head + [p] + tail
print(" ".join(str(x) for x in sortz))

#import random

##numItems=int(input())
#numItems=random.randint(1,1000)
#assert 1 <= numItems <= 1000
##array=[int(x) for x in input().split(' ')]
#array= random.sample(range(-1000,1000), numItems + 1) #add one for p...
#p=array[0]
#array.pop(0)
##input()
#head=[]
#tail=[]
#for i in range(0,p):
#    if p < i:
#        head.append(i)
#    if p > i:
#        tail.append(i)
#sortz = head + [p] + tail
#print(" ".join(str(x) for x in sortz))