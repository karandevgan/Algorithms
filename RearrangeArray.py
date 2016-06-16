class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        if len(A) == 1:
            return A
        for i in xrange(len(A)):
            A[i] += (A[A[i]] % len(A)) * len(A)
        for i in xrange(len(A)):
            A[i] = A[i] / len(A)
        return A

sol = Solution()
print sol.arrange([5,5,5,0,0,1])
