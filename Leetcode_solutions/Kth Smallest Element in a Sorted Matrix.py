class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        num = 1
        elems = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                elems.append(matrix[i][j])
        elems.sort()
        return elems[k - 1]
