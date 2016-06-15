import bisect
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        if len(A) == 1:
            return 1
        count = 0
        for i in xrange(0, len(A)-2):
            letters = sorted(A[i:])
            index = bisect.bisect_left(letters, A[i])
            if index != 0:
                permutation = 1
                for i in xrange(2, len(letters)):
                    permutation *= i
                count += index * permutation

        if A[len(A)-1] > A[len(A)-2]:
            count += 1
        else:
            count += 2
        return count % 1000003

sol = Solution()
print sol.findRank('ACD')
