import sys
numItemsArray=[]
arrayOfArrays=[]
with open("insertionSort.txt") as f:
    numTests = int( f.readline() )
    assert 1 <= numTests <= 5
    for i in range(0,numTests):
        numItemsArray.append( int( f.readline() ) )
        arrayOfArrays.append( [int(x) for x in f.readline().split()] )

""" 
EXPECTED OUTPUT: insertionSort.txt

46768
77
108411
16750
101598
"""
def merge_and_count(a, b):
    assert a == sorted(a) and b == sorted(b)
    c = []
    count = 0
    i, j = 0, 0
    while i < len(a) and j < len(b):
        c.append(min(b[j], a[i]))
        if b[j] < a[i]:
            count += len(a) - i # number of elements remaining in `a`
            j+=1
        else:
            i+=1
    # now we reached the end of one the lists
    c += a[i:] + b[j:] # append the remainder of the list to C
    return count, c

def sort_and_count(L):
    if len(L) == 1: return 0, L
    n = len(L) // 2 
    a, b = L[:n], L[n:]
    ra, a = sort_and_count(a)
    rb, b = sort_and_count(b)
    r, L = merge_and_count(a, b)
    return ra+rb+r, L


#numTests=int(input())
#assert 1 <= numTests <= 5
for _ in range(0,numTests):
    #numItems=int(input())
    numItems=numItemsArray[_]
    assert 1 <= numItems <= 100000
    #array=[int(x) for x in input().split(' ')]
    array=arrayOfArrays[_]
    #array.sort()

    answer,sortedArray = sort_and_count(array)
    print(answer)