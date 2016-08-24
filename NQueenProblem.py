class Solution:
    # @param A : integer
    # @return a list of list of strings
    def solveNQueens(self, A):
        return_list = []
        occupied_positions = []
        self.auxillary(A, 0, return_list, occupied_positions, [])
        return return_list
    
    def auxillary(self, A, no_of_queens_placed, return_list, occupied_positions, board):
        if no_of_queens_placed == A:
            return

        candidate_slots = [(no_of_queens_placed,j) for j in xrange(A)]

        for candidate in candidate_slots:
            if self.isCandidateValid(candidate, occupied_positions):
                new_board = board[:]

                position = self.createStringOfPositions(candidate[1], A)
                new_board.append(position)

                new_occupied_positions = occupied_positions[:]            
                new_occupied_positions.append(candidate)
                
                self.auxillary(A, no_of_queens_placed+1, return_list, new_occupied_positions, new_board)
                
                if len(new_board) == A:
                    return_list.append(new_board)
    
    def isCandidateValid(self, candidate, occupied_positions):
        for pos in occupied_positions:
            if candidate[0] == pos[0] or candidate[1] == pos[1] or \
                abs(candidate[0] - pos[0]) == abs(candidate[1] - pos[1]):
                return False
        return True
        
    def createStringOfPositions(self, queenColumn, A):
        i = 0
        position = [''] * A
        while i != queenColumn:
            position[i] = "."
            i += 1
        position[i] = "Q"
        i += 1
        while i != A:
            position[i] = "."
            i += 1
        return ''.join(position)

sol = Solution()
print sol.solveNQueens(5)