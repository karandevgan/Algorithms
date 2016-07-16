class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A.sort()
        return_list = []
        sum = 0
        for i in xrange(len(A)-2):
            if (i > 0 and A[i] == A[i-1]):
                continue
            j = i + 1
            k = len(A) - 1
            while (j < k):
                sum = A[i] + A[j] + A[k]
                if sum == 0:
                    return_list.append([A[i], A[j], A[k]])
                    j += 1
                    while (A[j] == A[j-1] and j < k):
                        j = j+1
                elif sum < 0:
                    j += 1
                else:
                    k -= 1
        return return_list

sol = Solution()
A = [-1, 0, 1, 2, -1, -4]
# -4, -1, -1, 0, 1, 2
print sol.threeSum(A)