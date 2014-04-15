
s=int(input())
assert 1 <= s <= 1000
array=[int(x) for x in input().split(' ')]
sortz=array[:1]
for i in range(1,len(array)):
    sortz.append(array[i])
    j=len(sortz)-1
    while sortz[j] < sortz[j-1] and j > 0:
        temp=sortz[j]
        sortz[j]=sortz[j-1]
        sortz[j-1]=temp
        j-=1
print(" ".join(str(x) for x in sortz))