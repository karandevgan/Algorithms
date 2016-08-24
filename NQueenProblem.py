class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        return_list = []
        invalid_positions = set([])
        self.auxillary(A, 0, return_list, invalid_positions, [])
        return return_list
    
    def auxillary(self, A, no_of_queens_placed, return_list, invalid_positions, board):
        if no_of_queens_placed == A:
            return

        candidate_slots = [(no_of_queens_placed,j) for j in xrange(A)]

        for candidate in candidate_slots:
            if self.isCandidateValid(candidate, invalid_positions):
                new_board = board[:]

                position = self.createStringOfPositions(candidate[1], A)
                new_board.append(position)

                new_invalid_positions = set(invalid_positions)            
                self.updateInvalidPositions(new_invalid_positions, candidate, A)
                
                self.auxillary(A, no_of_queens_placed+1, return_list, new_invalid_positions, new_board)
                
                if len(new_board) == A:
                    return_list.append(new_board)
    
    def isCandidateValid(self, candidate, invalid_positions):
        return candidate not in invalid_positions
        
    def createStringOfPositions(self, queenColumn, A):
        i = 0
        position = []
        while i != queenColumn:
            position.append(".")
            i += 1
        position.append("Q")
        while i != A-1:
            position.append(".")
            i += 1
        return ''.join(position)

    def updateInvalidPositions(self, invalid_positions, candidate, A):
        # Adds invalid points in the same col
        for j in xrange(candidate[0]+1, A):
            invalid_positions.add((j, candidate[1]))
        
        # Adds invalid points on right diagonal
        row = candidate[0]
        col = candidate[1]
        while row != A-1 and col != A-1:
            row += 1
            col += 1
            invalid_positions.add((row, col))
        
        # Adds invalid points on left diagonal
        row = candidate[0]
        col = candidate[1]
        while row != A-1 and col != 0:
            row += 1
            col -= 1
            invalid_positions.add((row, col))

sol = Solution()
print sol.solveNQueens(4)