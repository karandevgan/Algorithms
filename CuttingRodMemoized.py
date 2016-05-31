import random

random.seed(100)

price = [random.randint(1,100) for _ in range(100)]
length = [i for i in range(1,101)]

price_per_length = {key:value for key,value in zip(length, price)}

def CutRod(length):
    computed_lengths = {key: None for key in range(1,length+1)}
    return CutRodMemoized(length, computed_lengths)

def CutRodMemoized(length, computed_lengths):
    if length == 0:
        optimised_cost = 0
    else:
        if computed_lengths[length] is not None:
            return computed_lengths[length]

        optimised_cost = float("-inf")
        for i in range(1, length+1):
            optimised_cost = max(optimised_cost, price_per_length[i] + CutRodMemoized(length-i, computed_lengths))

    computed_lengths[length] = optimised_cost
    return optimised_cost

print CutRod(20)
