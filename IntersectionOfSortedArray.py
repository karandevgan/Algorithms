class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        if len(A) < len(B):
            A,B = B,A

        return_list = []
        i = 0
        j = 0
        while (i != len(A) and j != len(B)):
            if A[i] == B[j]:
                return_list.append(A[i])
                i += 1
                j += 1
            elif A[i] < B[j]:
                i += 1
            else:
                j += 1

        return return_list

sol = Solution()
A = [1,2,3,3,4,5,6]
B = [0]
print sol.intersect(A,B)