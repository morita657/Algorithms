class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        output = []
        for i in range(len(nums)):
            current = nums[i]
            for j in range(i + 1, len(nums)):
                current *= nums[j]
                output.append(current)
        return max(output)


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    self.dfs(i, j, grid, time)
        return time

    def dfs(self, i, j, board, time):
        if i < 0 or i > len(board) or j < 0 or j > len(board[0]) or board[i][j] != 1:
            return
        return self.dfs(i + 1, j, board, time + 1) +\
            self.dfs(i, j + 1, board, time + 1) +\
            self.dfs(i - 1, j, board, time + 1) +\
            self.dfs(i, j - 1, board, time + 1)
