# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            right = self.maxDepth(root.right)
            left = self.maxDepth(root.left)
            return max(left, right) + 1


s = Solution()
s.maxDepth([3, 9, 20, None, None, 15, 7])
# print()
