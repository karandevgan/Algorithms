import random

random.seed(100)

price = [random.randint(1,100) for _ in range(100)]
length = [i for i in range(1,101)]

price_per_length = {key:value for key,value in zip(length, price)}

def CutRod(length):
    computed_lengths = [0]
    for rod_length in range(1, length+1):
        optimised_cost = float("-inf")
        for sub_rod_length in range (1, rod_length+1):
            print "Subrod1:", sub_rod_length, "Subrod2:", length - sub_rod_length
            optimised_cost = max(optimised_cost, price_per_length[sub_rod_length] + computed_lengths[rod_length - sub_rod_length])
        computed_lengths.append(optimised_cost)
    return computed_lengths[length]

print CutRod(20)
