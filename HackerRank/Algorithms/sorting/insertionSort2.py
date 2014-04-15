numItems=int(input())
assert 1 <= numItems <= 1000
array=[int(x) for x in input().split(' ')]
insertThis = array[-1]
i=len(array)-2
while insertThis < array[i] and i >= 0:
    array[i+1]=array[i]
    i-=1
    print(" ".join(str(x) for x in array))
array[i+1]=insertThis
print(" ".join(str(x) for x in array))