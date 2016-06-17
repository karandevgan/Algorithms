import math
def sqrt(A):
    if A*A == A:
        return A
    low = 0.0
    high = float(A)
    epsilon = 0.0005
    A = float(A)
    num = (low + high) / 2.0
    diff = (abs(num * num) - A)

    while (diff > epsilon):
        if (num * num > A):
            high = num
        elif (num * num < A):
            low = num

        num = (low + high) / 2.0
        diff = abs((num * num) - A)
    num = int(num)
    if (num+1) ** 2 == A:
        return num+1
    return num
print sqrt(234234234)
