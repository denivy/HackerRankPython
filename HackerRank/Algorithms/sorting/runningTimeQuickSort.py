####################################################
class Swaps:
    def __init__(self):
        self.counter=0
    def inc(self):
        self.counter += 1
    def getCount(self):
        return self.counter
####################################################
def quickSort(array2):
    if len(array2) <= 1:
        return
    pivot=array2[-1]
    part=0
    for i in range(0,len(array2)):
        if array2[i] <= pivot:
            temp=array2[i]
            array2[i]=array2[part]
            array2[part]=temp
            swaps.inc()        
            part+=1
    quickSort(array2[:part-1]) 
    quickSort(array2[part:])
##################################################    
numItems=int(input())
array=[int(x) for x in input().split(' ')]
assert 1 <= numItems <= 1000
array2 = array.copy()
shifts=0
swaps=Swaps()

for i in range(1,len(array)):
    j=i

    while array[j] < array[j-1] and j > 0:
        value=array[j]
        array[j] = array[j-1]
        array[j-1]=value
        j-=1
        shifts+=1

quickSort(array2)
print(shifts-(swaps.getCount()))