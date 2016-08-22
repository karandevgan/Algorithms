class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        A.sort()
        return_list = []
        return_list.append(A)
        
        if len(A) <= 1:
            return return_list
        
        while True:
            A = self.generateNextPermutation(A[:])

            if A == return_list[0]:
                break
            return_list.append(A)
        
        return return_list
        
    
    def generateNextPermutation(self, A):
        i = len(A) - 2
        j = len(A) - 1
        while (A[i] > A[j]):
            i -= 1
            j -= 1
        A[j:] = sorted(A[j:])
        
        while A[j] < A[i]:
            j += 1
        A[j], A[i] = A[i], A[j]
        return A


sol = Solution()
print sol.permute([1,2,3])