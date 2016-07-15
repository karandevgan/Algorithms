class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        # import pdb
        # pdb.set_trace()
        if len(A) == 0 or len(A) == 1:
            return len(A)

        count = 1
        i = 1
        while i < len(A):
            if A[i] == A[i-1]:
                count += 1
            else:
                count = 1
            if count > 2:
                break
            i += 1

        if i == len(A):
            return len(A)
        
        j = i+1
        while True:
            if j == len(A):
                break
            count = 1
            while j < len(A):
                if A[j] == A[j-1]:
                    j += 1
                else:
                    break
            
            if j == len(A):
                break

            while j < len(A)-1:
                if A[j] == A[j+1]:
                    count = 2
                    j += 1
                else:
                    break

            A[i], A[j] = A[j], A[i]
            i += 1
            if count == 2:
                A[i], A[j-1] = A[j-1], A[i]
                i += 1
            j += 1

        return i

sol = Solution()
#A = [1,2,3,4,5,6]
#A = [1,1,1]
A = [1,1,1,1,1,1,1,1,1,1,1,1,1,2]
print sol.removeDuplicates(A)