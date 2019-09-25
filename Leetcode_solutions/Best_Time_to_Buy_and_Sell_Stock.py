import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = math.inf
        maxprofit = 0
        for i in range(len(prices)):
            if prices[i] < minprice:
                minprice = prices[i]
            elif prices[i] - minprice > maxprofit:
                maxprofit = prices[i] - minprice
        return maxprofit


import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        current = 0
        maxsofar = 0
        for i in range(1, len(prices)):
            current = max(current + prices[i] - prices[i - 1], 0)
            maxsofar = max(maxsofar, current)
        return maxsofar
