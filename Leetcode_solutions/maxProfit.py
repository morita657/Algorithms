class Solution:
    def maxProfit(self, prices):
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    def maxProfit2(self, prices):
        i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        while i < len(prices) - 1:
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            peak = prices[i]
            maxprofit += peak - valley
        return maxprofit


s = Solution()
# print(s.maxProfit([7, 1, 5, 3, 6, 4]))
print(s.maxProfit([1, 7, 2, 3, 6, 7, 6, 7]))
print(s.maxProfit2([1, 7, 2, 3, 6, 7, 6, 7]))
