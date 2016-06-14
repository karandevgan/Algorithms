class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if A==0 or B==0:
            return max(A,B)
        dividend = max(A, B)
        divisor = min(A,B)
        remainder = dividend % divisor
        while (remainder != 0):
            dividend = max(divisor, remainder)
            divisor = min(divisor, remainder)
            remainder = dividend % divisor
        return divisor


sol = Solution()
print sol.gcd(13,9)
