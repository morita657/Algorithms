class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] in d.keys():
                if d[s[i]] == t[i]:
                    continue
                else:
                    return False
            else:
                if t[i] in d.values():
                    return False
                else:
                    d[s[i]] = t[i]
        return True
