class Solution:
    def maxAreaOfIsland(self, grid):
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ans = max(ans, self.search(i, j, grid))
        return ans

    def search(self, i, j, board):
        if (i < 0 or i >= len(board)) or(j < 0 or j >= len(board[0])):
            return 0
        if board[i][j] == 0:
            return 0
        board[i][j] = 0
        return 1 + self.search(i - 1, j, board) +\
            self.search(i, j - 1, board) +\
            self.search(i + 1, j, board) +\
            self.search(i, j + 1, board)


s = Solution()
s.maxAreaOfIsland([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0],
                   [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]])
