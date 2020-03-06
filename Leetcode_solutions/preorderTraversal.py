# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        output=[]
        def search(node, o):
            if node == None:
                return
            else:
                o.append(node.val)
            if node.left:
                search(node.left, o)
            if node.right:
                search(node.right, o)
        output=[root.val]
        search(root.left, output)
        search(root.right, output)
        return output

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        stack,output =[root],[]
        while len(stack)>0:
            now = stack.pop()
            if now is not None:
                output.append(now.val)
                if now.right:
                    stack.append(now.right)
                if now.left:
                    stack.append(now.left)
        return output

    def inorder(root):
        res = []
        stack = []
        curr = root
        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res