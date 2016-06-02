def repeatedNumbers(A):
    sumOfGivenNumbers = long(0)
    sumOfOriginalNumbers = long(0)

    sumOfSquaresOfGivenNumbers = long(0)
    sumOfSquaresOfOriginalNumbers = long(0)

    for num in A:
        sumOfGivenNumbers += num
        sumOfSquaresOfGivenNumbers += long(num) * long(num)
    for num in range(1, len(A) + 1):
        sumOfOriginalNumbers += num
        sumOfSquaresOfOriginalNumbers += long(num) * long(num)

    diffOfSum = sumOfOriginalNumbers - sumOfGivenNumbers
    diffOfSumOfSquares = sumOfSquaresOfOriginalNumbers - sumOfSquaresOfGivenNumbers

    equation1 = diffOfSum
    equation2 = -(diffOfSumOfSquares) / equation1

    doubleNumber = -(equation1 + equation2) / 2
    missingNumber = (equation1 - equation2) / 2

    return [int(doubleNumber), int(missingNumber)]


A = [i for i in range(1,535)]
A[533] = 1
print len(A)

print repeatedNumbers(A)
