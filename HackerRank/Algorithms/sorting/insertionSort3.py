#numItems=int(input())
numItems = 9
assert 1 <= numItems <= 1000
#array=[int(x) for x in input().split(' ')]
array=[9, 8, 6, 7, 3, 5, 4, 1, 2]
for i in range(1,len(array)):
    j=i
    #print("--")
    #print("array=",array,"i=",i,"j=",j,"array[i]=",array[i],"array[i-1]=",array[i-1])
    while array[j] < array[j-1] and j > 0:
        value=array[j]
        array[j] = array[j-1]
        array[j-1]=value
        j-=1
        #print("array=",array,"i=",i,"j=",j,"array[j]=",array[j],"array[j-1]=",array[j-1])
    print(" ".join(str(x) for x in array))