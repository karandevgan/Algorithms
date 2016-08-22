class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        if A == 0:
            return []

        decimal_list = []
        for i in xrange(2**A):
            decimal_list.append((i>>1)^i)
        # binary_list = self.auxillary(A)
        # decimal_list = [int(num, 2) for num in binary_list]
        return decimal_list


    # def auxillary(self, A):
    #     return_list = ["0", "1"]
    #     if A == 1:
    #         return return_list
    #     intermediate_list = self.auxillary(A-1)
    #     return_list = []
    #     for item in intermediate_list:
    #         return_list.append("0" + item)
        
    #     for item in intermediate_list[::-1]:
    #         return_list.append("1" + item)
    #     return return_list

sol = Solution()
print sol.grayCode(3)