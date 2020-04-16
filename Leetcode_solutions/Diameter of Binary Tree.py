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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            self.ans = max(self.ans, l+r+1)
            return max(l,r)+1
        dfs(root)
        return self.ans - 1