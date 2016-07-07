class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        A = A.lower()
        if len(A) <= 1:
            return A

        start = 0
        end = 0
        maxLength = 0
        for i in xrange(1,len(A)):
            low = i-1
            high = i
            while (low >= 0 and high < len(A) and A[low] == A[high]):
                if (high - low + 1 > maxLength):
                    maxLength = high - low + 1
                    start = low
                    end = high
                low -= 1
                high += 1
            
            low = i-1
            high = i+1
            while (low >= 0 and high < len(A) and A[low] == A[high]):
                if (high - low + 1 > maxLength):
                    maxLength = high - low + 1
                    start = low
                    end = high
                low -= 1
                high += 1
        return A[start:end+1]

sol = Solution()
A = "aba"
print sol.longestPalindrome(A)