size=int(input())
dict=[]
assert 1 <= size <= 1000000
for i in range(0,size):#for each line of input
    nums, strs = input().split()
    dict.append([ int(nums), strs ])
for x in range(0,len(dict)//2):
    dict[x][1]='-'
answer=""    
for x in sorted(dict, key=lambda x: x[0]):
    answer += x[1] + ' '
print (answer.strip())
    
#size=int(input())
#print("size=",size)
#print("len(numbers)=",len(numbers),"len(strings)=",len(strings),'len(dict)=',len(dict))
#print("numbers=",numbers)
#print("strings=",strings)
#print("dict=",dict)
#input

