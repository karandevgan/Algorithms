class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        low = 0
        high = len(A) - 1
        mid = 0
        while (low <= high):
            mid = low - (low - high) / 2
            if (A[mid] == B):
                return mid
            elif A[mid] > B:
                high = mid - 1
            else:
                low = mid + 1
        return low
sol = Solution()
A = [1]
print sol.searchInsert(A, 2)
