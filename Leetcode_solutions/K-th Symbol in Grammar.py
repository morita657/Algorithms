class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        row = [0]
        currentRow = 0
        while currentRow < N:
            currentRow += 1
            for r in range(len(row) - 1, -1, -1):
                if row[r] == 0:
                    row.insert(r + 1, 1)
                else:
                    row.insert(r + 1, 0)
        print(row)
        return row[K - 1]


class Solution(object):
    def kthGrammar(self, N, K):
        if N == 1:
            return 0
        return (1 - K % 2) ^ self.kthGrammar(N - 1, (K + 1) // 2)
