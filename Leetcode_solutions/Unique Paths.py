class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        if m < 1 or n < 1:
            return 0
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None] * (n + 1) for i in range(m + 1)]

        def move(movem, moven, dp):
            if dp[movem][moven] != None:
                return dp[movem][moven]
            if movem == 1 and moven == 1:
                return 1
            if movem < 1 or moven < 1:
                return 0
            dp[movem][moven] = move(movem - 1, moven, dp) + \
                move(movem, moven - 1, dp)
            return dp[movem][moven]
        return move(m, n, dp)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1 for i in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]
        print(dp)
        return dp[n - 1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def helper(i, j):
            if (i, j) in memo:
                return memo[i, j]
            ans = 0
            if i < m:
                ans += helper(i + 1, j)
            if j < n:
                ans += helper(i, j + 1)
            if i == m and j == n:
                ans += 1
            memo[i, j] = ans
            return memo[i, j]
        return helper(1, 1)
