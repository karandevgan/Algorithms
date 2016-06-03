def plusone(A):
    index = 0
    while True:
        if A[index] == 0 and len(A) > 1:
            print "Removing 0", A
            A = A[index+1:]
        else:
            break;
    for index in range(len(A) - 1, -1, -1):
        print "Adding ", A
        if (A[index] == 9):
            A[index] = 0
            if index == 0:
                newA = [1]
                newA.extend(A)
                A = newA
        else:
            A[index] += 1
            break
    return A
A = [0, 6, 0, 6, 4, 8, 8, 1]

A = plusone(A)

print A
