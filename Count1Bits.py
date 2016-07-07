class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        if A == 0:
            return 0
        if A == 1:
            return 1
        count = 0
        while (A != 0):
            if (A % 2 == 1):
                count += 1
            A = A/2
        return count

sol = Solution()
print sol.numSetBits(11)