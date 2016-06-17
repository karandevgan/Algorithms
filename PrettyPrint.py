class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        length = A * 2 - 1
        matrix = [None] * (length)
        for i in xrange(length):
            matrix[i] = [0 for _ in xrange(length)]
        mid = A-1
        value = 0
        for i in xrange(mid+1):
            value = A - i
            for j in xrange(i, length-i):
                matrix[i][j] = value
                matrix[j][i] = value
        for i in xrange(length-1, mid, -1):
            value = A - (length - i - 1)
            for j in xrange(i, length-i-2, -1):
                matrix[i][j] = value
                matrix[j][i] = value
        return matrix

sol = Solution()
print sol.prettyPrint(10)
