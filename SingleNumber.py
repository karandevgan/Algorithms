class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        result = 0
        for num in A:
            result = result ^ num
        return result

sol = Solution()
A = [1,1,2,2]
print sol.singleNumber(A)