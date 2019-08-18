class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        q, m, n = [], len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = 0x7fffffff
                else:
                    q.append((i, j))
#         q is not empty?
        for i, j in q:
            #         walk around adjacent elements
            for r, c in ((i, 1 + j), (i, j - 1), (i + 1, j), (i - 1, j)):
                #         original location +1, (collected locations are originally 0)
                z = matrix[i][j] + 1
#     adjacent location is bigger than native loc +1 ?
                if 0 <= r < m and 0 <= c < n and matrix[r][c] > z:
                    #         assign the orignal + 1 value to the adjacent ones
                    matrix[r][c] = z
#     then move to the locations and check their adjacents
                    q.append((r, c))
        return matrix
