class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        o = []
        for i in range(len(coins)):
            self.dfs([], coins, o, amount)
        if len(o) > 0:
            return min(o)
        else:
            return -1

    def dfs(self, current, coins, output, amount):
        if sum(current) == amount and len(current) not in output:
            output.append(len(current))
            return
        if sum(current) > amount:
            return
        else:
            for i in range(len(coins)):
                self.dfs(current + [coins[i]], coins, output, amount)


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
