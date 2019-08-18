class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        output = []
        level = 0
        self.dfs(root, level, output)
        current = output[0][0]
        index = 1
        for i in range(1, len(output)):
            # print sum(output[i]), current
            if sum(output[i]) > current:
                current = sum(output[i])
                # print current
                index = i + 1
        return index

    def dfs(self, root, level, output):
        if (root == None):
            return output
        # if len(output) <= level and len(root) > 0:
        output.append([])
        output[level].append(root.val)
        if root.left:
            self.dfs(root.left, level + 1, output)
        if root.right:
            self.dfs(root.right, level + 1, output)
