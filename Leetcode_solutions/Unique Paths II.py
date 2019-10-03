class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        ans = 0
        dp = [[None] * (len(obstacleGrid[0]))
              for _ in range(len(obstacleGrid))]
        return self.dfs(obstacleGrid, len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1, dp)

    def dfs(self, board, i, j, dp):
        if i < 0:
            self.dfs(board, i + 1, j, dp)
        if j < 0:
            self.dfs(board, i, j + 1, dp)
        if i == 1 and j == 1:
            return 1
        if dp[i][j] != None:
            return dp[i][j]
        dp[i][j] = self.dfs(board, i - 1, j, dp) + \
            self.dfs(board, i, j - 1, dp)
        return dp[i][j]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        memo, m, n = {}, len(obstacleGrid), len(obstacleGrid[0])

        def helper(i, j):
            if (i, j) in memo:
                return memo[i, j]
            ans = 0
            if obstacleGrid[i - 1][j - 1] == 0:
                # if not obstacleGrid[i - 1][j - 1]:
                if i < m:
                    ans += helper(i + 1, j)
                if j < n:
                    ans += helper(i, j + 1)
                if i == m and j == n:
                    ans += 1
            memo[i, j] = ans
            return memo[i, j]

        return helper(1, 1)


s = Solution()
s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
