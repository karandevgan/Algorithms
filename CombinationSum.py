class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A.sort()
        return self.generateList(A, B)


    def generateList(self, A, B):
        l = []
        if B in A:
            l.append([B])
        for i in xrange(len(A)-1):
            if i > 0 and A[i] == A[i-1]:
                continue            
            diff = B - A[i]
            if diff >= A[i+1]:
                temp = self.generateList(A[i+1:], diff)
                if len(temp):
                    for item in temp:
                        l.append([A[i]] + item)
            else:
                break
        return l

sol = Solution()
A = [ 8, 10, 6, 11, 1, 16, 8 ]

print sol.combinationSum(A, 28)