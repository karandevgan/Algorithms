class Solution:
    # @param n : integer
    # @param k : integer
    # @return a strings
    def getPermutation(self, n, k):
        if n == 0:
            return ''

        self.factorials = [1]
        for i in xrange(1, n):
            self.factorials.append(i * self.factorials[i-1])

        A = [str(i) for i in xrange(1, n+1)]
        l = self.auxillary(A, k, [])
        return ''.join(l)
    
    def auxillary(self, A, k, result_list):
        if k == 1:
            for item in A:
                result_list.append(item)
            return result_list

        permutation_per_number = self.factorials[len(A)-1]
        candidate = k / permutation_per_number
        if candidate * permutation_per_number == k:
            candidate -= 1
        result_list.append(A[candidate])
        del A[candidate]
        k = k - (candidate * permutation_per_number)
        return self.auxillary(A, k, result_list)


sol = Solution()
print sol.getPermutation(3,4)