# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        output = []
        level = 0

        def bfs(node, output, level):
            if node == None:
                return
            else:
                if len(output) - 1 < level:
                    output.append([])
                output[level].append(node.val)
                bfs(node.left, output, level + 1)
                bfs(node.right, output, level + 1)
        bfs(root, output, 0)
        return output
