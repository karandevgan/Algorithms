class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        row_of_digits = {str(i):[] for i in xrange(1,10)}
        col_of_digits = {str(i):[] for i in xrange(1,10)}
        block_of_digits = {(i,j):[] for i in xrange(0,9) for j in xrange(0,9)}

        for row_index, row in enumerate(A):
            if len(row) != 9:
                return 0
            for col_index, digit in enumerate(row):
                if digit == '.':
                    continue
                digit_row = row_of_digits[digit]
                if row_index in digit_row:
                    return 0
                digit_row.append(row_index)
                row_of_digits[digit] = digit_row
                
                digit_col = col_of_digits[digit]
                if col_index in digit_col:
                    return 0
                digit_col.append(col_index)
                col_of_digits[digit] = digit_col
                
                block = block_of_digits[(row_index/3, col_index/3)]
                if digit in block:
                    return 0
                block.append(digit)
                block_of_digits[(row_index/3, col_index/3)] = block
        return 1
                

sol = Solution()
A = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
print sol.isValidSudoku(A)