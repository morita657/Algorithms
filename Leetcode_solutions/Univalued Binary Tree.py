# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.bfs(root)

    def bfs(self, node):
        uniVal = node.val
        q = [node]
        flag = True
        while len(q) > 0:
            now = q.pop(0)
            if now.val != uniVal or now.val == None:
                flag = False
                break
            if now.left:
                q.append(now.left)
            if now.right:
                q.append(now.right)
        return flag
