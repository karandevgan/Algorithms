class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        power = len(A) - 1
        col_num = 0
        for alphabet in A:
            col_num += (26**power) * (ord(alphabet) - ord('A') + 1)
            power -= 1
        return col_num



sol = Solution()
print sol.titleToNumber('AZAZHDW')
print sol.titleToNumber('BBA')
