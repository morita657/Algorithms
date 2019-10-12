class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1]]
        for i in range(2, rowIndex + 2):
            current = [1 for _ in range(i)]
            for j in range(len(current)):
                if j == 0 or j == len(current) - 1:
                    current[j] = 1
                else:
                    current[j] = ans[-1][j] + ans[-1][j - 1]
            ans.append(current)
        return ans[rowIndex]
