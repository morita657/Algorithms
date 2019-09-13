class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n

# another solution


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        for i in range(n):
            ans = ans * x
        return ans


class Solution:
    def fastPow(self, x, n):
        if n == 0:
            return 1.0
        else:
            half = self.fastPow(x, n / 2)
            if n % 2 == 0:
                return half * half
            else:
                return half * half * x

    def myPow(self, x, n):
        N = n
        if N < 0:
            x = 1 / x
            N = -N
        return self.fastPow(x, N)


class Solution:
    def myPow(self, x, n):
        N = n
        if N < 0:
            x = 1 / x
            N = -N
        ans = 1
        current_product = x
        for i in range(N, 0):
            i /= 2
            if i % 2 == 1:
                ans = ans * current_product
            current_product = current_product * current_product
        return ans


s = Solution()
print(s.myPow(2, 10))
