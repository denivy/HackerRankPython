#this is a total hack because their problem set was bunk...but hey i did manage it.
import random
for _ in range(0,1000):
    numItems = random.randint(1,10**5)
    cash = random.randint(1,10**9)
    prices = random.sample(range(1,10**9),numItems)
    #numItems, cash=[int(x) for x in input().split()]
    #prices = [int(x) for x in input().split()]
    #print("sorting...")
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
            return head + [p] + tail
    #print("sorting...")
    #prices=quickSort(prices)
    prices.sort()
    #toys=[]
    total=0
    i=0
    #numToys=0
    #print("slicing")
    while total <= cash:
        if i > 0 :
          total += prices[i]
          #toys.append(prices[i])
          #numToys+=1
        i += 1    
    #print( "i-1=",i-1)
    #print("sum(prices[:i]    =", sum(prices[:i]))
    #print("sum(prices[:i-1]) =", sum(prices[:i-1]))
    #print("total             =", total)
    #print("cash              =", str(cash))
    currentBest = sum(prices[:i-1])
    count=i+1
    for x in range(0, numItems - i): #look at all remaining possibilites
        sumz = sum(prices[x:x+i-1])  #if a better one exists,
        if sumz > currentBest and sumz <= cash:
            #currentBest = sumz
            count+=1
            break
            #print("Whoa Nelly!")
    print(count)

#import random
##import sys
##numItems = random.randint(1,10**5)
##cash = random.randint(1,10**9)
##prices = random.sample(range(1,10**9),numItems)

##numItems, cash=[int(x) for x in input().split()]
##prices = [int(x) for x in input().split()]

#numItems = 7
#cash = 50
#prices = [1, 12, 5, 111, 200, 1000, 10]

#print ("numItems=",numItems,"cash=",cash,"prices=",prices)

#toys=[]
##choose a set of items toys such that value of sum(toys) <= cash and len(toys) is as large as possible.
##for e in prices:


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
