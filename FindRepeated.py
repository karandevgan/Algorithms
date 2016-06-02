def repeatedNumber(A):
    numbers = {}
    for i in xrange(len(A)):
        value = numbers.get(A[i])
        if value is None:
            numbers[A[i]] = 1
        elif value == 1:
            return A[i]

print repeatedNumber([3, 4, 1, 4, 1])
