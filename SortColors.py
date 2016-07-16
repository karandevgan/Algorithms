class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        # Approach 1: Require 3 passes
        # B = []
        # for i in xrange(3):
        #     for color in A:
        #         if color == i:
        #             B.append(color)
        # return B

        first = 0
        last = len(A)-1
        i = 0
        while i < len(A):
            if A[i] == 0:
                while first < len(A) and A[first] == 0:
                    first += 1
                if i > first and first < len(A):
                    A[i], A[first] = A[first], A[i]
                    continue
            elif A[i] == 2:
                while last > 0 and A[last] == 2:
                    last -= 1
                if i < last and last > 0:
                    A[i], A[last] = A[last], A[i]
                    continue
            i += 1
        return A

sol = Solution()
import random
random.seed(4)

A = [random.randint(0,2) for _ in xrange(10)]
print A
print sol.sortColors(A)
0, 0, 1, 0, 0, 1, 2, 2, 2, 0