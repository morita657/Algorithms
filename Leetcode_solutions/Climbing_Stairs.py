class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [[] for i in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(n + 1)]
        dp[0] = 1

        def main(n, dp):
            if n == 0:
                return dp[n]
            if n <= 0:
                dp[n] = 0
                return dp[n]
            if dp[n] > 0:
                return dp[n]
            else:
                dp[n] = main(n - 1, dp) + main(n - 2, dp)
            return dp[n]
        return main(n, dp)


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(n + 1)]
        if n <= 1:
            return 1
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        return dp[n]
