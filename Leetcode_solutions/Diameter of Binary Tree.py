# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        level = 0
        # if root.left:
        left = self.dfs(root.left, level) if root.left else 0
        # if  root.right:
        right = self.dfs(root.right, level) if root.right else 0
        return left + right

    def dfs(self, node, height):
        if not node:
            return height
        else:
            left = self.dfs(node.left, height + 1)
            right = self.dfs(node.right, height + 1)
            return max(left, right)
