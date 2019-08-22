"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""

# Initiate the first and the last nodes as nulls.

# Call the standard inorder recursion helper(root):

# If node is not null:

# Call the recursion for the left subtree helper(node.left).

# If the last node is not null, link the last and the current node nodes.

# Else initiate the first node.

# Mark the current node as the last one: last = node.

# Call the recursion for the right subtree helper(node.right).

# Link the first and the last nodes to close DLL ring and then return the first node.


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):
            """
            Performs standard inorder traversal:
            left -> node -> right
            and links all nodes into DLL
            """
            nonlocal last, first
            if node:
                # left
                helper(node.left)
                # node
                if last:
                    # link the previous node (last)
                    # with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node
                    # to close DLL later on
                    first = node
                last = node
                # right
                helper(node.right)

        if not root:
            return None

        # the smallest (first) and the largest (last) nodes
        first, last = None, None
        helper(root)
        # close DLL
        last.right = first
        first.left = last

        return first
