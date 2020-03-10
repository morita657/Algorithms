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


    def reverse1(self, x: int) -> int:
        sign = 1
        target = str(x)
        target = list(target)
        if x < 0:
            sign = -1
            target = target[1:]
        left = 0
        right = len(target) - 1
        while left < right:
            target[left], target[right] = target[right], target[left]
            left += 1
            right -= 1
        target = "".join(target)
        target = int(target) * sign
        if target > 2147483647+1 or target < -2147483648-1:
            return 0
        return target