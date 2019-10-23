# public String longestPalindrome(String s) {
#     if (s == null | | s.length() < 1) return ""
#     int start = 0, end = 0
#     for (int i=0
#          i < s.length()
#          i + +) {
#         int len1 = expandAroundCenter(s, i, i)
#         int len2 = expandAroundCenter(s, i, i + 1)
#         int len = Math.max(len1, len2)
#         if (len > end - start) {
#             start = i - (len - 1) / 2
#             end = i + len / 2
#         }
#     }
#     return s.substring(start, end + 1)
# }

# private int expandAroundCenter(String s, int left, int right) {
#     int L = left, R = right
#     while (L >= 0 & & R < s.length() & & s.charAt(L) == s.charAt(R)) {
#         L - -
#         R + +
#     }
#     return R - L - 1
# }


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            length = max(len1, len2)
            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start:end + 1]

    def expandAroundCenter(self, s, left, right):
        L = left
        R = right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1
