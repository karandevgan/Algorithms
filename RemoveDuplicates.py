class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) < 1:
            return 0
            
        if len(A) == 1:
            return 1

        i = 1
        while (i < len(A) and A[i] != A[i-1]):
            i += 1
        
        if i == len(A):
            return len(A)
        
        j = i+1
        
        while j < len(A):
            while j < len(A) and A[j] == A[i]:
                j += 1
            if j < len(A):
                A[i], A[j] = A[j], A[i]
                j += 1
                i += 1
            while j < len(A) and A[i-1] == A[j]:
                j += 1
            if j == len(A):
                break
        
        return i