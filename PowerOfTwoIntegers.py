class Solution:
    def isPower(self, A):
        if A == 0:
            return False
        if A == 1:
            return True

        for i in xrange(2, 33):
            for j in xrange(2, int(A**(1.0/i)) + 2):
                if j**i == A:
                    return True
        return False

sol = Solution()
print sol.isPower(1024000000)
