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


    def firstUniqChar1(self, s: str) -> int:
        d = collections.defaultdict(int)
        for i in range(len(s)):
            d[s[i]] += 1
        for j in range(len(s)):
            if d[s[j]]==1:
                return j
        return - 1
        
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for i, ch in enumerate(s):
            if count[ch]==1:
                return i
        return -1