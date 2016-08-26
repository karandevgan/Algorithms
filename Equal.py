class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        dict_sums = {}
        result = []
        for i in xrange(len(A)):
            for j in xrange(i+1, len(A)):
                sum = A[i] + A[j]
                list_of_indices = dict_sums.get(sum, [])
                isPairEligible = True
                if len(list_of_indices) > 0 and \
                (list_of_indices[0] == j or list_of_indices[1] == j or \
                list_of_indices[0] == i or list_of_indices[1] == i):
                    isPairEligible = False
                if isPairEligible:
                    candidate = [i,j]
                    if len(list_of_indices) < 4:
                        list_of_indices.extend(candidate)
                    else:
                        if candidate < list_of_indices[2:]:
                            list_of_indices[2:] = candidate
                    if len(list_of_indices) == 4 and (result == [] or result > list_of_indices):
                        result = list_of_indices
                    dict_sums[sum] = list_of_indices
        return result

sol  = Solution()
A = [9, 5, 4, 9, 3, 6, 8, 7, 1, 2, 8, 7, 2, 9, 7, 1, 3, 9, 7, 8, 1, 0, 5, 5]
print sol.equal(A)