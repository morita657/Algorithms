# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output = []
        self.rec(root, output)
        return output

    def rec(self, root, output):
        if root is None:
            return []
        if root.left is not None:
            self.rec(root.left, output)
        output.append(root.val)
        if root.right is not None:
            self.rec(root.right, output)
