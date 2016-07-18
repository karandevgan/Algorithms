class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        max_area = 0
        left = 0
        right = len(A) - 1
        while (left < right):
            max_area = max(max_area, (right-left) * min(A[left], A[right]))
            if A[left] < A[right]:
                left += 1
            else:
                right -= 1
        return max_area
A = [1,5,4,3]
sol = Solution()
print sol.maxArea(A)