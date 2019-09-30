class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = 0
        cands = list(set(J))
        for stone in S:
            if stone in cands:
                jewels += 1
        return jewels
