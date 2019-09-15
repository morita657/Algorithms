class Solution:
    def reverse(self, x: int) -> int:
        op = "+"
        num = str(x)
        if x < 0:
            op = str(x)[0]
            num = str(x)[1:]
        num = num[::-1]
        ans = op + num
        if int(ans) > 2**31 - 1 or int(ans) < -2**31:
            return 0
        else:
            return int(ans)
