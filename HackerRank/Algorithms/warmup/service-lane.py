import random
import bisect
###################################
#numPackets = int(input())
#numPackets = 7
numPackets = random.randint(1,10**5)
###################################
assert 1 < numPackets < 10**5
#######################################
#kids = int(input())
#kids = 3
kids = random.randint(1,numPackets)
########################################
assert 1 < kids < numPackets
packets_chosen=[]
input_array = [10,100,300,200,1000,20,30]
maxValue=maxKey=minkey=0
minValue=10**9
for i in range(0,numPackets):    
    ################################3
    #numCandies = int(input())
    #numCandies = input_array[i]
    numCandies = random.randint(0, 10**9)
    #####################################
    #print ("numCandies=",numCandies,"currentMax=",currentMax)
    assert 0 <= numCandies <= 10**9
    #build a list of items with length equal to the number of kids.  keep track of the index and the value of the current highest values and lowest values
    if len(packets_chosen) < kids:
        bisect.insort(packets_chosen,numCandies)
        #packets_chosen[i]=numCandies
        #is it the biggest?
        
    else:
        #once the list is built, the only time we update it is if we find a value that is smaller than one we already have
        diff = packets_chosen[-1] - packets_chosen[0]
        
        if numCandies - packets_chosen[0] < diff: #if the difference is smaller than our current max...
            #print("HERE")
            packets_chosen.pop()#pop one off
            packets_chosen.append(numCandies)#add one on
            i=len(packets_chosen)-1 #find the length, and subtract one
            while packets_chosen[i] < packets_chosen[i-1]: #shift it into place
                swap = packets_chosen[i]
                packets_chosen[i] = packets_chosen[i-1]
                packets_chosen[i-1] = swap
                i-=1
        elif packets_chosen[-1] > numCandies > packets_chosen[0]: #or bigger than our current min...
            #print("THERE")
            packets_chosen.pop(0) #pop the first element.
            packets_chosen.insert(0,numCandies) #insert a new one
            i=0
            while packets_chosen[i] > packets_chosen[i+1]:
                swap = packets_chosen[i]
                packets_chosen[i] = packets_chosen[i+1]
                packets_chosen[i+1] = swap
                i+=1
            
    #print("numCandies=",numCandies)
    #print("minVal=",minValue,"maxVal=",maxValue)
    #print("minKey=",minKey,"maxKey=",maxKey)
            #maxKey = packets_chosen[-1]
        #elif numCandies > currentMin:
        #    currentMin,minIndex = numCandies,i
    #print("packets_chosen=",packets_chosen,"maxIndex=",maxIndex,"currentMax=",currentMax,"minIndex=", minIndex, "currentMin=",currentMin)
    #print("packets_chosen=",packets_chosen)
print(max(packets_chosen) - min(packets_chosen))