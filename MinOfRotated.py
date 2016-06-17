class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        if len(A) == 1:
            return A[0]
        low = 0
        high = len(A) - 1
        while low <= high:
            if A[low] <= A[high]:
                return A[low]
            mid = low - (low - high) / 2
            next = (mid + 1) % len(A)
            prev = (mid + len(A) - 1) % len(A)
            if (A[mid] <= A[next] and A[mid] <= A[prev]):
                return A[mid]
            elif (A[mid] < A[high]):
                high = mid - 1
            elif (A[mid] > A[low]):
                low = mid + 1


sol = Solution()
print sol.findMin([ 1,2,3,4,5,6,0 ])
