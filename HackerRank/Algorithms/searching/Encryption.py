#message = "ifmanwasmeanttostayonthegroundgodwouldhavegivenusroots"
#message = "haveaniceday"
#message = "feedthedog"
#message = "chillout"
import math
message=input()
length = len(message)
assert 1 <= length <= 81

floorz = int(math.sqrt(length))
ceilz = int(math.ceil(math.sqrt(length)))

if floorz is not ceilz:
    if floorz < ceilz and floorz * ceilz >= length:
        rows,cols = floorz,ceilz
    else:
        rows,cols = ceilz,ceilz
else: rows,cols = floorz,floorz

encode=[]
answer=  dict.fromkeys(range(cols),"")

for x in range(rows):
    encode = (message[(x*cols):((x*cols) + cols)])
    for y in range(len(encode)):
        answer[y] += encode[y]
print (" ".join(answer.values()))
#print("y=",y,"encode[y]=",encode[y])
#print ("encode=",encode)
#print ("answer=",answer)
#print("length=",length,"rows=",rows, "cols=",cols)
