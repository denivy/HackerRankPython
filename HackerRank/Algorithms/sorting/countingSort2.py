size=int(input())
assert 100 <= size <= 1000000
numbers=[int(x) for x in input().split()]
counters={}
counts=""
for x in range(0,100):
    counters[x] = 0
for e in numbers:
    counters[e] += 1
for y in counters:
    counts += (str(y)+' ')*counters[y]
print(counts.strip())