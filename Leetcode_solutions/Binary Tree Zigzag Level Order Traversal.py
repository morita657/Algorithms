# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        def bfs(node, o, level):
            if node == None:
                return
            else:
                if len(o) == level:
                    o.append([])
                o[level].append(node.val)
                bfs(node.left, o, level + 1)
                bfs(node.right, o, level + 1)
        output = []
        bfs(root, output, 0)
        for i in range(len(output)):
            if i % 2 != 0:
                output[i] = output[i][::-1]
        return output
