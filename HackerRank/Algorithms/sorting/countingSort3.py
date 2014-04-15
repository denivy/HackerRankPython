size=int(input())
numbers=[]
assert 1 <= size <= 1000000
for i in range(0,size):#for each line of input
    nums, strs = input().split()
    numbers.append(int(nums))
counters={}
for x in range(0,100):
    counters[x] = 0
for e in numbers:
    counters[e] += 1
counts=""
total=0
for z in counters: #for each element of counters...
    total += counters[z]
    counts += str(total) + ' '
print(counts.strip() )


###import random
###import sys
##size=int(input())
###size=random.randint(1,1000000)
##numbers=[]
###strings=[]
###with open('inputData.txt', 'r') as f:
###    size=int(f.readline())
###    for line in f:
###        #print('line=',line,'line.split()=',line.split() )
###        nums,strs=line.split()
###        #print ("nums=",nums, "strs=",strs)
###        numbers.append(int(nums))
###        strings.append(strs)
##assert 1 <= size <= 1000000
##for i in size:#for each line of input
##    nums, strs = input().split()
##    numbers.append(int(nums))
##    #strings.append(strs)
###print('size=',size)
###print('numbers=',numbers)
###print('strings=',strings)
##counters={}
##for x in range(0,100):
##    counters[x] = 0
##for e in numbers:
##    counters[e] += 1
##counts=""
##total=0
##for z in counters: #for each element of counters...
##    total += counters[z]
##    counts += str(total) + ' '
###print ("counters=",counters)
###counts="" #to be printed to screen
###for y in counters: #for each counter...
###    counts += (str(y) + ' ') * counters[y]  #print the number of occurences, + sum of the number of occurances of all preceding elements....

##print(counts.strip() )
