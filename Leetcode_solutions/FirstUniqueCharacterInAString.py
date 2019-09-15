class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.defaultdict(int)
        for i in range(len(s)):
            d[s[i]] += 1
        flag = True
        for index, key in enumerate(d):
            if d[key] == 1:
                flag = False
                return s.index(key)
        if flag:
            return -1
