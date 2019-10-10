class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            current = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    current.append(1)
                else:
                    current.append(ans[-1][j] + ans[-1][j - 1])
            ans.append(current)
        return ans
