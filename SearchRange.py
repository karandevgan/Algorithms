class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers

    def searchRange(self, A, B):
        low = 0
        high = len(A) - 1
        start_index = -1
        last_index = -1
        first_occurence = -1
        while (low <= high):
            mid = low - (low - high) / 2
            if A[mid] == B:
                start_index = mid
                if first_occurence == len(A):
                    first_occurence = mid
                high = mid - 1
            elif A[mid] > B:
                high = mid - 1
            else:
                low = mid + 1

        if start_index == -1:
            return [-1, -1]

        low = first_occurence
        high = len(A) - 1

        while (low <= high):
            mid = low - (low - high) / 2
            if A[mid] == B:
                last_index = mid
                low = mid + 1
            elif A[mid] > B:
                high = mid - 1
            else:
                low = mid + 1

        return [start_index, last_index]

sol = Solution()
A = [5,7,7,8,10,10,10]
print sol.searchRange(A,10)
