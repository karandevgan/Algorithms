class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        count = 0
        sum = 0

        # Every number can be represented in 32 bits.
        for bit in xrange(32):
            # Count all the numbers whose ith bit is set
            for num in A:
                if (num & (1 << bit)):
                    count += 1
            # (len(A) - count) numbers will have ith bit as 0
            # count * (len(A) - count) will give sum of difference between ith bit
            sum += count * (len(A)-count) * 2
            count = 0
        
        return_mod = (10 ** 9) + 7
        return sum % return_mod

A = [1,3,5]
sol = Solution()
print sol.cntBits(A)