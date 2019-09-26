class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        if m < 1 or n < 1:
            return 0
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        aux = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                aux[i][j] = aux[i][j - 1] + aux[i - 1][j]
        return aux[-1][-1]
