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
            