class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        alpha = []
        non_alpha = []
        for i in range(len(S)):
            if S[i].isalpha():
                # alpha.insert(0, (len(S)-1-i, S[i]))
                alpha.insert(0, S[i])
            else:
                non_alpha.append((i, S[i]))
        ans = ""
        index = 0
        while index < len(S):
            if len(non_alpha) > 0 and index == non_alpha[0][0]:
                ans += non_alpha[0][1]
                non_alpha.pop(0)
            else:
                ans += alpha[0]
                alpha.pop(0)
            index += 1
        return ans
