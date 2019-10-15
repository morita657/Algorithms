"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []
        if root == None:
            return output
        if root.children == None:
            return [root.val]
        self.search(root.children, output)
        output.append(root.val)
        return output

    def search(self, node, ans):
        for i in range(len(node)):
            if node[i].children == None:
                ans.append(node[i].val)
            else:
                self.search(node[i].children, ans)
                ans.append(node[i].val)
        return ans
