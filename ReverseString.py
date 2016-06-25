class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        list_of_words = A.split()
        list_of_words.reverse()
        return ' '.join(list_of_words)

sol = Solution()
print sol.reverseWords("")
