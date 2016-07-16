class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        lowest_point = 0
        for i in xrange(len(A) -1):
            j = len(A) - 1
            while (A[j] - A[i] >= B and j > lowest_point):
                if A[j] - A[i] == B:
                    return 1
                j -= 1
            lowest_point = max(i+1, j)
        return 0

sol = Solution()

A = [0,2,3]
B = 1
print sol.diffPossible(A,B)