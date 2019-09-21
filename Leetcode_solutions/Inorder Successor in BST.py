# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderSuccessor(self, root, p, flag=False):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if root:
            if flag:
                return root.val
            if p.val == root.val:
                flag = True
            self.inorderSuccessor(root.left, p, flag)
            self.inorderSuccessor(root.right, p, flag)
        # return None
