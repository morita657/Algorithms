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
        traverse = root
        while traverse:
            if traverse.val == val:
                return traverse
            else:
                if val > traverse.val:
                    traverse = traverse.right
                else:
                    traverse = traverse.left
