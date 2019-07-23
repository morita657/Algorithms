class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                print j
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        # print count
        print grid
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


# Solution()
solution = Solution()
solution.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], [
                    "1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
