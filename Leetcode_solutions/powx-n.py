class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        for i in range(n):
            ans = ans * x
        return ans
