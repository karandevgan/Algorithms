from collections import deque
 
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        if len(A) == 0:
            return ([[]])
 
        A.sort()
        subset_dict = deque()
        subset_dict.appendleft([A[-1]])
 
        for i in xrange(len(A)-2, -1, -1):
            j = -1
            for _ in xrange(len(subset_dict)):
                item = subset_dict[j]
                temp_item = [A[i]] + item
                if temp_item not in subset_dict:
                    subset_dict.appendleft(temp_item)
                j -= 1
            if A[i] != A[i+1]:
                subset_dict.appendleft([A[i]])
        subset_dict.appendleft([])
        return list(sorted(subset_dict))
A = [1,2,2,2]
print Solution().subsetsWithDup(A)