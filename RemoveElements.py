class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        i = 0
        j = 0
        while j < len(A):
            if A[i] == B:
                if A[j] != B:
                    A[i], A[j] = A[j], A[i]
                    i += 1
            else:
                i += 1
            j += 1
        A =  A[:i]
        return i

sol = Solution()
A = [100,100]

print sol.removeElement(A,3)