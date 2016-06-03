def MultiplyMatrix(A, B):
    n = len(A[0]) # number of cols of A = number of rows of B
    m = len(A) # number of rows of A
    r = len(B)
    p = len(B[0]) # number of cols of  B

    if (n != r):
        print "Error: Matrices not compatible"
        return []

    C = []

    for i in range(m):
        C.append([])
        for j in range(p):
            temp = 0
            for k in range(n):
                temp += A[i][k] * B[k][j]
            C[i].append(temp)
    return C

def PrintMatrix(A):
    if len(A) > 0:
        n = len(A[0]) # no of cols
        m = len(A) # no of rows
        for i in range(m):
            for j in range(n):
                print A[i][j],
            print "\n"

A = [[1,2,3],[4,5,6]]
B = [[7,8],[9,10],[11,12]]

C = MultiplyMatrix(A, B)
PrintMatrix(C)
