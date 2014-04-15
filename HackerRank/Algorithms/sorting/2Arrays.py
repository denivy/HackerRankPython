numTests = int(input())
assert 1 <= numTests <= 10
for _ in range(numTests):
    howMany, maxValue = [int(x) for x in (input().split())]
    A=[int(x) for x in (input().split())]
    B=[int(x) for x in (input().split())]
    assert 1 <= howMany <= 1000
    assert 1 <= maxValue <= 10**9
    assert len(A) == howMany and len(B) == howMany
    A.sort()
    B.sort(reverse=True)
    conditionMet="YES"
    for e in range(len(A)): #for each element in a
        if A[e] + B[e] < maxValue:
            conditionMet="NO"
    print(conditionMet)




##import random
##numTests = random.randint(1,10)
##numTests = 2
##howManyMaxVals=[(3,10),(4,5)]
##Avals=[ [2,1,3], [1,2,2,1] ]
##Bvals=[ [7,8,9], [3,3,3,4] ]
#numTests = int(input())
#assert 1 <= numTests <= 10
#for _ in range(numTests):
#    #howMany = random.randint(1,1000)
#    #maxValue = random.randint(1,10**9)
#    #A = random.sample(range(0,10**9),howMany)
#    #B = random.sample(range(0,10**9),howMany)
#    #howMany,maxValue = howManyMaxVals[_]
#    #A = Avals[_]
#    #B = Bvals[_]
#    howMany, maxValue = int(input())
#    A=int(input())
#    B=int(input())
#    assert 1 <= howMany <= 1000
#    assert 1 <= maxValue <= 10**9
#    assert len(A) == howMany and len(B) == howMany
#    A.sort()
#    B.sort(reverse=True)
#    conditionMet="YES"
#    for e in range(len(A)): #for each element in a
#        if A[e] + B[e] < maxValue:
#            conditionMet="NO"
#    print(conditionMet)











##import random
###numTests = int(input())
##numTests = random.randint(1,5)
##assert 1 <= numTests <= 5
##for _ in range(0,numTests):
##  #numItems=int(input())
##  #numItems = 9
##  numItems = random.randint(1,100000)
##  assert 1 <= numItems <= 100000
##  #array=[int(x) for x in input().split(' ')]
##  #array=[9, 8, 6, 7, 3, 5, 4, 1, 2]
##  array = random.sample(range(1,1000000),numItems)
##  array2 = sorted(array)
##  count=0
##  for i in array:
##      count += abs(i - array2.index(i))
##      #j=i
##      ##print("--")
##      ##print("array=",array,"i=",i,"j=",j,"array[i]=",array[i],"array[i-1]=",array[i-1])
##      #while array[j] < array[j-1] and j > 0:
##      #    value=array[j]
##      #    array[j] = array[j-1]
##      #    array[j-1]=value
##      #    j-=1
##      #    count+=1
##      #    #print("array=",array,"i=",i,"j=",j,"array[j]=",array[j],"array[j-1]=",array[j-1])
##      #print(" ".join(str(x) for x in array))
##  print(count)




##import random
###numTests = int(input())
###numTests = random.randint(1,10)
##numTests = 2
##assert 1 <= numTests <= 10
##howMany=[(3,10),(4,5)]
##Avals=[ [2,1,3], [1,2,2,1] ]
##Bvals=[ [7,8,9], [3,3,3,4] ]
##for _ in numTests:
##    #howMany, maxValue = int(input())
##    #A=int(input())
##    #B=int(input())
##    #howMany = random.randint(1,1000)
##    #maxValue = random.randint(1,10**9)
##    #A = random.sample(range(0,10**9),howMany)
##    #B = random.sample(range(0,10**9),howMany)
##    howMany,maxValue = howMany[_]
##    A = Avals[_]
##    B = Bvals[_]
##    assert 1 <= howMany <= 1000
##    assert 1 <= maxValue <= 10**9
##    assert len(A) == howMany and len(B) == howMany
##    print("A=",A,"B=",B)

##    A.sort()
##    B.sort()
