class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        divisor = 5
        zeroes = 0
        while (A != 0):
            zeroes += A / divisor
            A = A / divisor
        return zeroes

sol = Solution()
print sol.trailingZeroes(125)
