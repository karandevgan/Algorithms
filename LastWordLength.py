class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        wordStart = len(A)-1
        wordEnd = len(A)-1
        maxLength = 0
        length = 0
        for i in xrange(len(A)-1, -1, -1):
            if A[i] == ' ' or i == 0:
                if i == 0 and A[i] != ' ':
                    length = wordEnd - wordStart + 1
                else:
                    length = wordEnd - wordStart
                maxLength = max(maxLength, length)
                wordStart = i-1
                wordEnd = i-1
                if i != len(A) - 1 and maxLength != 0:
                    break
            else:
                wordStart -= 1
        return maxLength

sol = Solution()
print sol.lengthOfLastWord("")
