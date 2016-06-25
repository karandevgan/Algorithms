def consecutiveSum(A):
    num1 = A[0]
    num2 = A[1]
    num3 = A[2]
    candidate_sum = num1 + num2 + num3
    if len(A) > 3:
        for i in xrange(3, len(A)):
            temp = A[i]
            temp_sum = num2 + num3 + temp
            num1, num2 = num2, num1
            num2, num3 = num3, num2
            num3 = temp
            candidate_sum = max(temp_sum, candidate_sum)
    return candidate_sum

A = [4,7,2,1,5,6,20]
print consecutiveSum(A)
