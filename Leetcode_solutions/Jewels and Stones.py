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

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = list(set(J))
        res=0
        for i in range(len(jewels)):
            for j in range(len(S)):
                if S[j] == jewels[i]:
                    res += 1
        return res


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jset = set(J)
        return sum(s in jset for s in S)