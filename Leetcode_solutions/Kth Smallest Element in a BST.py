Kth Smallest Element in a BST
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        elems = []

        def bfs(root, els):
            if root == None:
                return
            else:
                els.append(root.val)
                bfs(root.left, els)
                bfs(root.right, els)
        bfs(root, elems)
        elems.sort()
        return elems[k - 1]
