class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        size = len(matrix) + len(matrix[0])
        ans = []
        flag = False
        for k in range(size):
            if flag:
                flag = False
                i = 0
                j = k
                while i <= k and j >= 0:
                    if i < len(matrix) and j < len(matrix[0]):
                        ans.append(matrix[i][j])
                    i += 1
                    j -= 1
            else:
                flag = True
                i = k
                j = 0
                while j <= k and i >= 0:
                    if i < len(matrix) and j < len(matrix[0]):
                        ans.append(matrix[i][j])
                    j += 1
                    i -= 1

        return ans
