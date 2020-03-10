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

import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h = collections.defaultdict(int)
        for i in range(len(s)):
            h[s[i]] += 1
        for j in range(len(t)):
            if not h[t[j]] or h[t[j]]<=0:
                return False
            else:
                h[t[j]] -= 1
        return True