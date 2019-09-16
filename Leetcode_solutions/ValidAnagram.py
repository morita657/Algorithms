class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cand = []
        for i in range(len(s)):
            cand.append(s[i])
        for j in range(len(t)):
            if t[j] in cand:
                index = cand.index(t[j])
                cand.pop(index)
            else:
                return False
        return len(cand) == 0
