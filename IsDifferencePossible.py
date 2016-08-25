class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        d = {}
        for index, integer in enumerate(A):
            number_of_occurences = d.get(integer, 0)
            number_of_occurences += 1
            d[integer] = number_of_occurences

        for integer in A:
            candidate = integer - B
            number_of_occurences = d.get(candidate, 0)
            
            if candidate == integer and number_of_occurences > 1:
                return 1
            elif candidate != integer and number_of_occurences > 0:
                return 1
                
        return 0
        


sol = Solution()
A = (0, 0, 1,5,3)
B = 0
print sol.diffPossible(A, B)
