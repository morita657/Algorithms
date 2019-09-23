

class Solution:
    # Time O amount * len(coins)
    # Space O amount
    def coinChange(self, coins, amount):
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1 and (dp[i] == -1 or dp[i - coin] + 1 < dp[i]):
                    dp[i] = dp[i - coin] + 1
        return dp[-1]


s = Solution()
s.coinChange([1, 2, 5], 11)
