class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer

    def uniquePaths(self, A, B):
        if A > B:
            B,A = A,B
        self.grid = [None] * A

        for i in xrange(A):
            self.grid[i] = [0] * B

        pos = (0,0)
        return self.calculatePaths(pos, A, B)

    def calculatePaths(self, pos, A, B):
        if (pos[0] == A-1 or pos[1] == B-1):
            return 1
        if self.grid[pos[0]][pos[1]] != 0:
            return self.grid[pos[0]][pos[1]]
        pos1 = (pos[0] + 1, pos[1])
        pos2 = (pos[0], pos[1] + 1)
        self.grid[pos[0]][pos[1]] = self.calculatePaths(pos1, A, B) + self.calculatePaths(pos2, A, B)
        return self.grid[pos[0]][pos[1]]

sol = Solution()
print sol.uniquePaths(14,12)
