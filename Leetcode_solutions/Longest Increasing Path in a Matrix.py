class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        dp = [[] * len(matrix[0]) for i in range(len(matrix))]

        def dfs(matrix, i, j):
            ans = 0
            for d in dirs:
                x = i + d[0]
                y = j + d[1]
                if 0 <= x and x < m and 0 <= y and y < n and matrix[x][y] > matrix[i][j]:
                    ans = max(ans, dfs(matrix, x, y))
            ans += 1
            return ans

        if len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(matrix, i, j))
        return ans


class Solution:
    def longestIncreasingPath(self, matrix):
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < M -1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < N - 1 and val > matrix[i][j + 1] else 0
                    )
            return dp[i][j]

        if not matrix or not matrix[0]:
            return 0
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for i in range(M)]
        return max(dfs(x, y) for x in range(M) for y in range(N))
