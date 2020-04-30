class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        ans=0
        start=0
        for i in range(len(s)):
            if len(s[start:i+1]) == len(set(s[start:i+1])):
                ans = max(ans, len(s[start:i+1]))
            else:
                start+=1
        return ans