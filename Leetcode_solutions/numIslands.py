# DFS
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


Solution()
solution = Solution()
solution.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], [
                    "1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])


class Solution(object):
    def numIslands(self, grid):
        count = 0
        for r in xrange(len(grid)):
            for c in xrange(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    self.dfs(grid, r, c)
        print count
        return count

    def dfs(self, grid, r, c):
        if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])) or grid[r][c] == "0":
            return
        grid[r][c] = "0"
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)


solution = Solution()
solution.numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], [
                    "1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
