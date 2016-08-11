class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        l = []
        A.sort()
        return self.auxillary(A, B)

    def auxillary(self, A, B):
        l = []
        for i in xrange(len(A)):
            if i > 0 and A[i] == A[i-1]:
                continue
            diff =  B - A[i]
            if diff < A[i]:
                break
            temp = self.auxillary(A[i:], diff)
            if len(temp):
                for item in temp:
                    l.append([A[i]] + item)
        if B in A:
            l.append([B])

        return l

sol = Solution()
A = [4,8,2,3,1,10,15]
B = 12
print sol.combinationSum(A, B)