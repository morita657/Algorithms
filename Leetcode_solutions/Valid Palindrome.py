class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
        sample = []
        for i in range(len(s)):
            if re.match(r'\w', s[i]) != None:
                if re.match('[A-Z]', s[i]) != None:
                    sample.append(s[i].lower())
                else:
                    sample.append(s[i])
        original = sample[:]
        if original == sample[::-1]:
            return True
        return False