#import random

#numFlowers= random.randint(1,1000000)
#numPeople = random.randint(1,100)
#prices = random.sample(range(1,1000000), numFlowers)

#numFlowers=3
#numPeople=3
#prices = [2,5,6]
#expected output = 13

#numFlowers=50
#numPeople=3
#prices=[int(x) for x in "390225 426456 688267 800389 990107 439248 240638 15991 874479 568754 729927 980985 132244 488186 5037 721765 251885 28458 23710 281490 30935 897665 768945 337228 533277 959855 927447 941485 24242 684459 312855 716170 512600 608266 779912 950103 211756 665028 642996 262173 789020 932421 390745 433434 350262 463568 668809 305781 815771 550800".split()]
#expected output = 163578911

numFlowers, numPeople = [int(x) for x in input().split()]
prices = [int(x) for x in input().split()]

assert 1 <= numFlowers
assert numPeople <= 1000000
assert len(prices) == numFlowers

cost=0
roundz=0
prices.sort(reverse=True)

for x in range(numFlowers):
    #print("round=", roundz, "x=", x, "prices[x]=", prices[x], "costThisRound=", prices[x] * (roundz + 1))
    cost += prices[x] * (roundz + 1)
    if (x + 1) % numPeople == 0: roundz += 1
print(cost)