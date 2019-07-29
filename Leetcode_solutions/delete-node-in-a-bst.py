# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.val == key:

            if root.left:
                temp = root.right
                root = root.left
                root.right = temp
                return root
            elif root.right:
                temp = root.left
                root = root.right
                root.left = temp
                return root
            else:
                return None
        if root and root.left:
            root.left = self.deleteNode(root.left, key)
        if root and root.right:
            root.right = self.deleteNode(root.right, key)
        return root
