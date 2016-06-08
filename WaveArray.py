def wave(A):
    A.sort()
    for i in xrange(0, len(A), 2):
        if i < len(A)-1:
            A[i], A[i+1] = A[i+1], A[i]
    return A
