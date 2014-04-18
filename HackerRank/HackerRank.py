import math, sys, filecmp
numbers = []
actions = []
with open("median-1.txt", 'r') as f:
   numOps = int(f.readline())
   for _ in range(numOps):
       act, num = [ x for x in f.readline().split() ]
       actions.append(act)
       numbers.append(int(num))

#print("actions=",actions)
#print("numbers=",numbers)

assert numOps == len(actions) == len(numbers)

def medianz(Lst):
    global f
    length = len(Lst)
    if length == 0: return
    elif length == 1: print ( int(Lst[0]) )
    else:
        midPoint = length / 2
        #print("L before=",L)    
        middle = math.ceil(midPoint) # does nothing if length is odd..otherwise rounds up
        #print("length=",length,"midPoint=",midPoint,"middle=",middle)
        for i in range(middle + 1):
            minIndex = i
            minVal = Lst[i]

            for j in range( i+1,length ) :
                if Lst[j] < minVal:
                    minIndex = j
                    minVal = Lst[j]

            temp = Lst[i]
            Lst[i] = Lst[minIndex]
            Lst[minIndex] = temp
        
        #print("L after=",L)
        if length % 2 == 0: #even
            ans = ( L[middle-1] + L[middle] ) / 2
            if ans == int(ans):
                print( int(ans) )
            else:
                print ( ans )
            #return ( L[midPoint] + L[midPoint+1] ) / 2
        else: #odd
            print( int(L[int(midPoint)]) )
#############################################################################################################

L=[]
for x in range(len(actions)):
    action = actions[x]
    number = numbers[x]
    #print("----------")
    #f = open ("median-out.txt", "w")
    if action == 'r':
        try:
            #print ("action=",action, "Length=",len(L),"L=",L)
            L.remove(number)
            if len(L) == 0:
                print("Wrong!")
            medianz(L)
        except:
            print("Wrong!")
            #pass
            #print("Wrong!")
        #finally:
            #if len(L) == 0: print("Wrong")
            
    else: #action == a
        L.append(number)
        medianz(L)
    #input(">")
#print("files=",filecmp.cmp("median-out.txt","median-0result.txt"))