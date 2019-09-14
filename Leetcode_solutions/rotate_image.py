class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix) - 1):
            for j in range(i, len(matrix)):
                print(i, j)
                [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]]
        return matrix


s = Solution()
print(s.rotate([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
print(s.rotate([
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]))
