numPackets = int(input())
kids = int(input())
assert 1 < numPackets < 10**5
assert 1 < kids < numPackets
packets=[]
for i in range(0,numPackets):    #for every packet
    packets.append(int(input()))
packets.sort()
answer=10**15
for x in range(0, numPackets - kids + 1):
    diff=packets[x + kids -1] - packets[x]
    if diff < answer:
        answer=diff
print(answer)



##import random
#import bisect

####################################
##numPackets = int(input())
##kids = int(input())
####################################
##numPackets = 7
##kids = 3
##input_array = [10,100,300,200,1000,20,30]
#########################################
########################################
#numPackets = random.randint(1,10**5)
#kids = random.randint(1,numPackets)
#assert 1 < numPackets < 10**5
#assert 1 < kids < numPackets

#packets=[]
##maxValue=0
##maxKey=0
##minkey=0
##minValue=10**9

#for i in range(0,numPackets):    #for every packet
#    ################################
#    #numCandies = int(input())
#    #numCandies = input_array[i]
#    numCandies = random.randint(0, 10**9)   #generate a random number of candies
#    ################################
#    #print ("numCandies=",numCandies)
#    assert 0 <= numCandies <= 10**9
    
#    if len(packets) < kids:  #first just fill it with the appropriate number of items.        
#        bisect.insort(packets, numCandies)

#    else:

#        highest = packets[-1] 
#        lowest  = packets[0]
#        diff = highest - lowest

#        if numCandies > lowest and numCandies - lowest < diff:
#            packets.pop()
#            bisect.insort(packets,numCandies)            
#        elif numCandies < highest and highest - numCandies < diff:
#            packets.pop(0)
#            bisect.insort(packets,numCandies)
    
#print(max(packets) - min(packets))


##import random
##for _ in range (20):
##    #numPackets = int(input())
##    #numPackets = 7
##    numPackets = random.randint(1,10**5)
##    assert 1 < numPackets < 10**5
##    #kids = int(input())
##    #kids = 3
##    kids = random.randint(1,numPackets)
##    assert 1 < kids < numPackets
##    packets_chosen={}
##    #input_array = [10,100,300,200,1000,20,30]
##    maxValue=maxKey=minkey=0
##    minValue=10**9
##    for i in range(0,numPackets):    
##        #numCandies = int(input())
##        #numCandies = input_array[i]
##        numCandies = random.randint(0, 10**9)
##        #print ("numCandies=",numCandies,"currentMax=",currentMax)
##        assert 0 <= numCandies <= 10**9
##        #build a list of items with length equal to the number of kids.  keep track of the index and the value of the current highest values and lowest values
##        if len(packets_chosen) < kids:
##            packets_chosen[i]=numCandies
##            #is it the biggest?
##            if numCandies > maxValue:
##                maxValue = numCandies
##                maxKey = i
##            #is it the smallest
##            elif numCandies < minValue:
##                minValue = numCandies
##                minKey = i
##        else:
##            #once the list is built, the only time we update it is if we find a value that is smaller than one we already have
##            if numCandies-minValue < numCandies-maxValue: #if its smaller than our current max...
##                packets_chosen[maxKey]=numCandies
##                maxValue = numCandies
##            elif maxValue-numCandies < maxValue-minValue:
##                packets_chosen[minKey]=numCandies
##                minValue = numCandies
##                #maxKey = packets_chosen[-1]
##            #elif numCandies > currentMin:
##            #    currentMin,minIndex = numCandies,i
##        #print("packets_chosen=",packets_chosen,"maxIndex=",maxIndex,"currentMax=",currentMax,"minIndex=", minIndex, "currentMin=",currentMin)
##        #print("packets_chosen=",packets_chosen,"currentMax=",currentMax)
##    print(max(packets_chosen) - min(packets_chosen))