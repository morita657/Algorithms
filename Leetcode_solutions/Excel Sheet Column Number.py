# class Solution:
#     def titleToNumber(self, s: str) -> int:
#         ans = []
#         for i in range(len(s)):
#             if i != len(s) - 1:
#                 ans.append((ord(s[i]) - 64) * 26**(len(s) - 1 - i))
#             else:
#                 ans.append(ord(s[i]) - 64)
#         return sum(ans)


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = None
        self.List = {'val': self.val, 'next': None}


m = MyLinkedList()
print(m)
