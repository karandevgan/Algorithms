import random

def maximumGap(A):

    maximumGap = -1
    if len(A) < 2:
        return maximumGap
    for i in xrange(0,len(A)/2):
        for j in xrange(len(A)-1, i, -1):
            if j - i < maximumGap:
                if (j == len(A)-1):
                    return maximumGap
                break
            if A[i] <= A[j]:
                maximumGap = max(maximumGap, j-i)
                break
    return maximumGap

A = [random.randint(1,10) for _ in xrange(10)]
print A
print maximumGap(A)
