"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    answer = 0

    def maxDepth(self, root: 'Node', depth) -> int:
        if root == None:
            return
        if root.children == None:
            answer == max(answer, depth)
        for i in range(len(root.children)):
            self.maxDepth(root[i], depth + 1)
        return answer


# private int answer;		// don't forget to initialize answer before call maximum_depth
# private void maximum_depth(TreeNode root, int depth) {
#     if (root == null) {
#         return;
#     }
#     if (root.left == null && root.right == null) {
#         answer = Math.max(answer, depth);
#     }
#     maximum_depth(root.left, depth + 1);
#     maximum_depth(root.right, depth + 1);
# }
