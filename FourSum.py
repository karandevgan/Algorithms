class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        result = []
        A.sort()
        if len(A) < 4:
            return result
        for i in xrange(len(A)-3):
            if i != 0 and A[i] == A[i-1]:
                continue
            for j in xrange(i+1, len(A)-2):
                if j != i+1 and A[j] == A[j-1]:
                    continue
                ptr1 = j+1
                ptr2 = len(A) - 1
                while ptr1 < ptr2:
                    sum = A[i] + A[j] + A[ptr1] + A[ptr2]
                    if sum == B:
                        result.append([A[i], A[j], A[ptr1], A[ptr2]])
                        ptr1 += 1
                        while (ptr1 < ptr2 and A[ptr1] == A[ptr1-1]):
                            ptr1 += 1
                    elif sum < B:
                        ptr1 += 1
                    else:
                        ptr2 -= 1
        return result

sol  = Solution()
A = [ 9, -8, -10, -7, 7, -8, 2, -7, 4, 7, 0, -3, -4, -5, -1, -4, 5, 8, 1, 9, -2, 5, 10, -5, -7, -1, -6, 4, 1, -5, 3, 8, -4, -10, -9, -3, 10, 0, 7, 9, -8, 10, -9, 7, 8, 0, 6, -6, -7, 6, -4, 2, 0, 10, 1, -2, 5, -2 ]
print sol.fourSum(A, 0)