class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        list_numbers = []
        while (A > 0):
            if A%26 == 0:
                list_numbers.append(26)
                A = (A/26)-1
            else:
                list_numbers.append(A%26)
                A = A/26
        list_numbers.reverse()
        return_string = ''
        for num in list_numbers:
            if num == 0:
                num = 26
            return_string += chr(num-1+ord('A'))
        return return_string

sol = Solution()
print sol.convertToTitle(618751039)
