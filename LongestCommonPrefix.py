class Solution:
    # @param A : list of strings
    # @return a strings

    def longestCommonPrefix(self, A):
        longest_prefix = ''
        if len(A) < 1:
            return longest_prefix
        if len(A) == 1:
            return A[0]

        prefix_length = len(A[0])

        for i in xrange(prefix_length):
            prev = A[0][i]
            for j in xrange(1, len(A)):
                if len(A[j]) <= i:
                    return longest_prefix
                if A[j][i] != prev:
                    return longest_prefix
            longest_prefix += prev

        return longest_prefix


A = [
    'abc'
]

sol = Solution()
print sol.longestCommonPrefix(A)
