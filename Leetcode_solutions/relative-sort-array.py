class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        table = [[0] * (target + 1)
                 for i in range(d + 1)]  # Initialize all entries as 0

        for j in range(1, min(f + 1, target + 1)):  # Table entries for only one dice
            table[1][j] = 1

        # Fill rest of the entries in table using recursive relation
        # i: number of dice, j: sum
        for i in range(2, d + 1):
            for j in range(1, target + 1):
                for k in range(1, min(f + 1, j)):
                    table[i][j] += table[i - 1][j - k] % (10**9 + 7)

        # print(dt)
        # Uncomment above line to see content of table
        # print table[-1][-1]%(10**9+7)
        return table[-1][-1] % (10**9 + 7)
