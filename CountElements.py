class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
        start_index = self.binarySearch(A, B, True)
        last_index = self.binarySearch(A, B, False)
        if last_index >= 0 and start_index >= 0:
            return last_index - start_index + 1
        else:
            return 0

    def binarySearch(self, A, B, searchFirst):
        low = 0
        high = len(A)-1
        result = -1
        while (low <= high):
            mid = low - (low - high) / 2
            if (A[mid] == B):
                result = mid
                if searchFirst:
                    high = mid - 1
                else:
                    low = mid + 1
            elif (A[mid] > B):
                high = mid - 1
            else:
                low = mid + 1
        return result
A  = [ 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 9, 9, 10, 10, 10, 11 ]
sol = Solution()
print sol.findCount(A, 5)
