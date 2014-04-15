import random

##random generated
#numTests = random.randint(1,10**5)
#numbers = random.sample(range(1,10**10),numTests)
#Samples
#numTests = 3
#numbers=[5,7,8]
#user Entry
numbers=[]
numTests = int(input())
for i in range(0,numTests):
    numbers.append(int(input()))

for x in numbers: #for each number in the list...
    #print (x) 
    a,b=0,1
    #print ("fib sequence of x=")
    fib = [0,1]
    while a < x:    #generate a fibonacci sequence.
        fib[0]=fib[1] #only track the last two numbers in a fib sequence
        fib[1] = a
        a,b = b, a+b
    #print (fib)
    if fib[-1] + fib[-2] == x:
        print("IsFibo")
    else:
        print("IsNotFibo")
