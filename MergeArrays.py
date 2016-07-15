class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        # import pdb
        # pdb.set_trace()
        if len(A) < len(B):
            A, B = B, A
        i = 0
        j = 0
        k = -1
        C = []
        while (i != len(A) and j != len(B)):
            if A[i] >= B[j]:
                temp = A[i]
                if k < len(C) and k >= 0 and C[k] < B[j]:
                    A[i] = C[k]
                    k += 1
                else:
                    A[i] = B[j]
                    j += 1
                if k < 0:
                    k += 1
                C.append(temp)
            i += 1
        
        while j != len(B) and len(C) > 0 and k != len(C):
            if B[j] < C[k]:
                A.append(B[j])
                j += 1
            else:
                A.append(C[k])
                k += 1
        
        while j != len(B):
            A.append(B[j])
            j += 1
        while k != len(C) and len(C) > 0:
            A.append(C[k])
            k += 1

        return A

sol = Solution()
A = [-4, -3, 0]
B = [2]
print sol.merge(A,B)