# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if len(s) == 0:
#             return 0
#         if len(s) == 1:
#             return 1
#         output = []
#         for i in range(len(s)):
#             temp = s[i]
#             flag = True
#             for j in range(i + 1, len(s)):
#                 if not s[j] in tuple(temp):
#                     temp += s[j]
#                 else:
#                     flag = False
#                     output.append(temp)
#                     temp = ""
#                     break
#             if flag:
#                 output.append(temp)
#                 temp = ""
#         ans = collections.defaultdict(list)
#         for k in range(len(output)):
#             ans[len(output[k])].append(output[k])
#         last = len(ans.keys())
#         if last == 0:
#             last = 1
#         return len(ans[last][0])


# # public class Solution {
# #     public int lengthOfLongestSubstring(String s) {
# #         int n = s.length()
# #         int ans = 0
# #         for (int i=0
# #              i < n
# #              i + +)
# #         for (int j=i + 1
# #              j <= n
# #              j + +)
# #         if (allUnique(s, i, j)) ans = Math.max(ans, j - i)
# #         return ans
# #     }

# #     public boolean allUnique(String s, int start, int end) {
# #         Set < Character > set = new HashSet <> ()
# #         for (int i=start
# #              i < end
# #              i + +) {
# #             Character ch = s.charAt(i)
# #             if (set.contains(ch)) return false
# #             set.add(ch)
# #         }
# #         return true
# #     }
# # }
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         n = len(s)
#         ans = 0
#         for i in range(n):
#             for j in range(i + 1, len(n) + 1):
#                 if self.allUnique(s, i, j):
#                     ans = max(ans, j - i)
#                 return ans

#     def allUnique(self, s, start, end):
#         set = []
#         i = start
#         while i < end:
#             ch = s[i]
#             if ch in set:
#                 return False
#             set.append(ch)
#         return True


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         first = 0
#         second = 0
#         current = []
#         cand = []
#         if len(s) == 0:
#             return 0
#         while second < len(s):
#             current.append(s[second])
#             if len(list(set(current))) == len(current):
#                 second += 1
#             else:
#                 current.pop()
#                 cand.append(current)
#                 first = second
#                 current = []
#         ans = []
#         for i in range(len(cand)):
#             ans.append(len(cand[i]))
#         ans.sort()
#         return ans[-1]


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 0:
#             return 0
#         current = ""
#         memory = []
#         s = s.replace(" ", "*")
#         for i in range(len(s)):
#             current = s[i]
#             for j in range(i + 1, len(s)):
#                 if not s[j] in current:
#                     current += s[j]
#                 else:
#                     memory.append((len(current), current))
#                     current = s[j]
#             memory.append((len(current), current))
#         memory.sort()
#         return memory[-1][0]


# "abcabcbb"
# "bbbbb"
# "pwwkew"
# ""
# " a"


# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         start = maxLength = 0
#         usedChar = {}

#         for i in range(len(s)):
#             if s[i] in usedChar and start <= usedChar[s[i]]:
#                 start = usedChar[s[i]] + 1
#             else:
#                 maxLength = max(maxLength, i - start + 1)

#             usedChar[s[i]] = i

# return maxLength
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            # when char already in dictionary
            if ch in dic:
                # check length from start of string to index
                res = max(res, i - start)
                # update start of string index to the next index
                start = max(start, dic[ch] + 1)
            # add/update char to/of dictionary
            dic[ch] = i
        # answer is either in the begining/middle OR some mid to the end of string
        return max(res, len(s) - start)


s = Solution()
s.lengthOfLongestSubstring("abcabcbb")
