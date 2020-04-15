class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.remove(S) == self.remove(T)

    def remove(self, word):
        ans = []
        for ch in word:
            if ch != "#":
                ans.append(ch)
            elif ans:
                ans.pop()
        return "".join(ans)

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        first = ''
        second = ''
                
        def reader(strg):
            res=""
            for j in range(len(strg)):
                if strg[j] == "#":
                    res = res[:-1]
                else:
                    res += strg[j]
            return res
        
        first = reader(S)
        second = reader(T)
            
        return first == second
            
from itertools import zip_longest
class Solution(object):
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))