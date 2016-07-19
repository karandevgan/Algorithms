class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        # import pdb
        # pdb.set_trace()
        i = 0
        j = 0
        k = 0
        diff = None
        while (i < len(A) and j < len(B) and k < len(C)):
            minimum = min(A[i], B[j], C[k])
            maximum = max(A[i], B[j], C[k])
            candidate = maximum - minimum
            if diff is None or candidate < diff:
                diff = candidate
            if diff == 0:
                break
            if A[i] == minimum:
                i += 1
            elif B[j] == minimum:
                j += 1
            else:
                k += 1
        return diff