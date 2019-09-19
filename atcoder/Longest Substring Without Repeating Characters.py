class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        output = []
        for i in range(len(s)):
            temp = s[i]
            flag = True
            for j in range(i + 1, len(s)):
                if not s[j] in tuple(temp):
                    temp += s[j]
                else:
                    flag = False
                    output.append(temp)
                    temp = ""
                    break
            if flag:
                output.append(temp)
                temp = ""
        ans = collections.defaultdict(list)
        for k in range(len(output)):
            ans[len(output[k])].append(output[k])
        last = len(ans.keys())
        if last == 0:
            last = 1
        return len(ans[last][0])


# public class Solution {
#     public int lengthOfLongestSubstring(String s) {
#         int n = s.length()
#         int ans = 0
#         for (int i=0
#              i < n
#              i + +)
#         for (int j=i + 1
#              j <= n
#              j + +)
#         if (allUnique(s, i, j)) ans = Math.max(ans, j - i)
#         return ans
#     }

#     public boolean allUnique(String s, int start, int end) {
#         Set < Character > set = new HashSet <> ()
#         for (int i=start
#              i < end
#              i + +) {
#             Character ch = s.charAt(i)
#             if (set.contains(ch)) return false
#             set.add(ch)
#         }
#         return true
#     }
# }
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i + 1, len(n) + 1):
                if self.allUnique(s, i, j):
                    ans = max(ans, j - i)
                return ans

    def allUnique(self, s, start, end):
        set = []
        i = start
        while i < end:
            ch = s[i]
            if ch in set:
                return False
            set.append(ch)
        return True
