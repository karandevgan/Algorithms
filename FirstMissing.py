def firstMissingPositive(A):
    if (len(A) == 0):
        return 1
    elif (len(A) == 1):
        if (A[0] == 1):
            return 2
        else:
            return 1

    j = 0
    for i in xrange(len(A)):
        if A[i] <= 0 or A[i] > len(A):
            A[i], A[j] = A[j], A[i]
            A[j] = 0
            j += 1

    for i in xrange(j,len(A)):
        index = abs(A[i]) - 1
        if (A[index] > 0):
            A[index] = -A[index]
        elif A[index] == 0:
            A[index] = -1

    for i in xrange(len(A)):
        if A[i] >= 0:
            return i+1
    return len(A)+1

#A = [8,3,5,6,4,-1,1,2]
#A = [3,4,-1,1]
A = [1, 2, 0, 4, 5, 9]
print firstMissingPositive(A)
