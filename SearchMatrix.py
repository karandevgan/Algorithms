class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer

    def searchMatrix(self, A, B):
        row_length = len(A[0])
        for row_index in xrange(len(A)):
            if A[row_index][0] == B or A[row_index][row_length - 1] == B:
                return 1
            elif A[row_index][0] < B and A[row_index][row_length - 1] > B:
                low = 1
                high = row_length - 2
                while (low <= high):
                    mid = low - (low - high) / 2
                    if A[row_index][mid] == B:
                        return 1
                    elif A[row_index][mid] < B:
                        low = mid + 1
                    else:
                        high = high - 1
                break
            print row_index
        return 0

sol = Solution()
matrix = [[1,   2,  5,  7],
          [10, 11, 16, 20],
          [20, 30, 34, 50]
          ]
print sol.searchMatrix(matrix, 20)
