class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        # make square array
        i = 1
        candidates = []
        while i < n:
            candidates.append(i * i)
            i += 1
        # candidates.reverse()
        cnt = 0
        toCheck = {n}
        # print toCheck
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                print temp, toCheck, cnt
                for y in candidates:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x - y)
            toCheck = temp
        return cnt


s = Solution()
s.numSquares(12)
