# processed_rows = []
# processed_cols = []
#
# def setZeroes(A):
#     for i in xrange(len(A)):
#         if i not in processed_rows:
#             setAllZero = False
#             for j in xrange(len(A[0])):
#                 if j not in processed_cols:
#                     if (A[i][j]) == 0:
#                         setAllZero = True
#                         processed_rows.append(i)
#                         processed_cols.append(j)
#                         setColZero(A,i,j)
#             if (setAllZero):
#                 for j in xrange(len(A[0])):
#                     A[i][j] = 0
#     return A
#
# def setColZero(A,current_row,j):
#     for i in xrange(len(A)):
#         if i != current_row:
#             if i not in processed_rows:
#                 if A[i][j] == 0:
#                     processed_rows.append(i)
#                     setRowZero(A, i,j)
#                 else:
#                     A[i][j] = 0
#
#
# def setRowZero(A, i,current_col):
#     for j in xrange(len(A[0])):
#         if j != current_col:
#             if j not in processed_cols:
#                 if A[i][j] == 0:
#                     processed_cols.append(j)
#                     setColZero(A,i, j)
#                 else:
#                     A[i][j] = 0
#
# print setZeroes([[0,0],[1,1]])


class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        R =1
        C =1
        if (len(A) > 0 and len(A[0]) > 0):
            for col_index in range(len(A[0])):
                if A[0][col_index] == 0:
                    R = 0
                    break;
            for row_index in range(len(A)):
                if A[row_index][0] == 0:
                    C = 0
                    break;

            for row_index in range(1,len(A)):
                for col_index in range(0,len(A[0])):
                    if (A[row_index][col_index]) == 0:
                        A[0][col_index] = 0
                        A[row_index][0] = 0

            for row_index in range(len(A))[:0:-1]:
                if A[row_index][0] == 0:
                    for col_index in range(1,len(A[0])):
                        A[row_index][col_index] = 0
            for col_index in range(1,len(A[0])):
                if A[0][col_index] == 0:
                    for row_index in range(1, len(A)):
                        A[row_index][col_index] = 0

            if R == 0:
                for col_index in range(len(A[0])):
                    A[0][col_index] = 0
            if C == 0:
                for row_index in range(len(A)):
                    A[row_index][0] = 0
            return A

sol = Solution()
# A = [
#   [0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
#   [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0],
#   [0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
#   [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1],
#   [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1],
#   [0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
#   [1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1],
#   [0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1]
# ]

A = [[0,0],[1,1]]
print sol.setZeroes(A)
