class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        low = 0
        high = len(A) - 1
        while(low < high):
            if A[low].isalnum() and A[high].isalnum():
                if A[low].lower() == A[high].lower():
                    low += 1
                    high -= 1
                else:
                    return 0
            if not A[low].isalnum():
                low += 1
            if not A[high].isalnum():
                high -= 1
        return 1

sol = Solution()
print sol.isPalindrome('')
