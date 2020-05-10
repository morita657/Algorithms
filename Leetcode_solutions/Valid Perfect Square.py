import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        side = math.sqrt(num)
        total = int(side)*int(side)
        return total == num
        