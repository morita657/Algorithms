# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root and root.val == val:
            return root
        if root and val > root.val:
            return self.searchBST(root.right, val)
        if root and val < root.val:
            return self.searchBST(root.left, val)
        return None
