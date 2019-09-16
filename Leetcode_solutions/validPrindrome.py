class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        cand = []
        for i in range(len(s)):
            if s[i].isalnum():
                cand.append(s[i].lower())
        return cand == cand[::-1]
