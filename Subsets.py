from collections import deque

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        if len(A) == 0:
            return ([[]])

        A.sort()
        subset_dict = deque()
        subset_dict.appendleft([A[-1]])

        for i in xrange(len(A)-2, -1, -1):
            j = -1
            for _ in xrange(len(subset_dict)):
                item = subset_dict[j]
                subset_dict.appendleft([A[i]] + item)
                j -= 1
            subset_dict.appendleft([A[i]])
        subset_dict.appendleft([])
        return list(subset_dict)

sol = Solution()
A = []
print sol.subsets(A)