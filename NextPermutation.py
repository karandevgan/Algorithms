def nextPermutation(A):
        if len(A) <= 1:
            return A
        isDecreasing = True
        for i in xrange(len(A)-2,-1,-1):
            if A[i] < A[i+1]:
                isDecreasing = False
                index_of_smallest = i
                break

        if isDecreasing:
            A.sort()
        else:
            A[index_of_smallest+1:len(A)] = sorted(A[index_of_smallest+1:len(A)])
            for i in xrange(index_of_smallest+1, len(A)):
                if A[i] > A[index_of_smallest]:
                    A[i], A[index_of_smallest] = A[index_of_smallest], A[i]
                    break
        return A

A = [ 626, 436, 819, 100, 382, 173, 817, 581, 220, 95, 814, 660, 397, 852, 15, 532, 564, 715, 179, 872, 236, 790, 223, 379, 83, 924, 454, 846, 742, 730, 689, 112, 110, 516, 85, 149, 228, 202, 988, 212, 69, 602, 887, 445, 327, 527, 347, 906, 54, 460, 517, 376, 395, 494, 827, 448, 919, 799, 133, 879, 709, 184, 812, 514, 976, 700, 156, 568, 453, 267, 547, 8, 951, 326, 652, 772, 213, 714, 706, 972, 318, 768, 506, 59, 854, 422 ]
ans1 = nextPermutation(A)
print ans1
