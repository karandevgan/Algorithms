import random

random.seed(100)

price = [random.randint(1,100) for _ in range(100)]
length = [i for i in range(1,101)]

price_per_length = {key:value for key,value in zip(length, price)}

def CutRod(length):
    if length == 0:
        return 0
    optimised_cost = float("-inf")
    for i in range(1,length+1):
        optimised_cost = max(optimised_cost, price_per_length.get(i) + CutRod(length-i))
    return optimised_cost

print CutRod(10)
