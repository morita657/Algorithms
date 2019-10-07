# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if root == None:
            return None, None
        elif root.val <= V:
            bns = self.splitBST(root.right, V)
            root.right = bns[0]
            return root, bns[1]
        else:
            bns = self.splitBST(root.left, V)
            root.left = bns[1]
            return bns[0], root


(TreeNode{val: 2, left: TreeNode{val: 1, left: None, right: None}, right: None},
 TreeNode{val: 3, left: None, right: None})
