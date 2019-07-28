# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isValidBST(self, root, low=float('-inf'), high=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not low < root.val:
            return False
        if not root.val < high:
            return False
        return self.isValidBST(root.left, low, min(root.val, high)) and self.isValidBST(root.right, max(root.val, low), high)
