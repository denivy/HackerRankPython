import random
numItems = random.randint(1,10**5)
#numItems=int(input())
#numItems = 7
assert 1 <= numItems <= 10**5
#array=[int(x) for x in input().split(' ')]
#array=[5, 8, 1, 3, 7, 9, 2]
array = random.sample(range(-10**5,10**5), numItems)
print("starting sort...")
def quickSort(array):
    if len(array) == 1:
        return array
    else:
        p=array.pop(0)
        head=[]
        tail=[]
        for i in array:
            if p < i:
                tail.append(i)                
            if p > i:
                head.append(i)
        if len(head) != 0:
            head=quickSort(head)
        if len(tail) != 0:
            tail=quickSort(tail)
        #print(" ".join(str(x) for x in head + [p] + tail))
        return head + [p] + tail
print(quickSort(array))