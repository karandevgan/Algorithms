class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        # import pdb
        # pdb.set_trace()
        return_list = []
        next_i = B
        next_d = 1
        
        for i in xrange(len(A)):
            if A[i] == 'I':
                return_list.append(next_d)
                next_d += 1
            elif A[i] == 'D':
                return_list.append(next_i)
                next_i -= 1
        
        return_list.append(next_d)
        return return_list

sol = Solution()

B = [55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print B ==  sol.findPerm('DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD', 55)