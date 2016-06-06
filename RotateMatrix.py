def rotate(A):
    n = len(A)
    j = 0
    while j < n/2:
        for i in xrange(j,n-1-j):
            temp = A[i][j]
            A[i][j] = A[n-1-j][i]
            A[n-1-j][i] = A[n-1-i][n-1-j]
            A[n-1-i][n-1-j] = A[j][n-1-i]
            A[j][n-1-i] = temp
        j += 1
    return A

A = [[1,2],[3,4]]
rotate(A)
print A
