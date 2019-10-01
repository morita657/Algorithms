class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        string = [S[i] for i in range(len(S))]
        return self.search(string)

    def search(self, string):
        left = 0
        right = 1
        flag = False
        while right < len(string):
            if string[left] == string[right]:
                string = string[:left] + string[right + 1:]
                flag = True
            left += 1
            right += 1
            if flag:
                flag = False
                left = 0
                right = 1
        return ''.join(string)


class Solution:
    def removeDuplicates(self, S: str) -> str:
        output = []
        for ch in S:
            if output and ch == output[-1]:
                output.pop()
            else:
                output.append(ch)
        return ''.join(output)
