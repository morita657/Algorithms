class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) % 2 == 1:
            return False
        for i in s:
            if i == "(":
                stack.append(")")
            elif i == "[":
                stack.append("]")
            elif i == "{":
                stack.append("}")
            if len(stack) > 0:
                if i == ")" and stack[len(stack) - 1] == ")":
                    stack.pop(len(stack) - 1)
                elif i == "]" and stack[len(stack) - 1] == "]":
                    stack.pop(len(stack) - 1)
                elif i == "}" and stack[len(stack) - 1] == "}":
                    stack.pop(len(stack) - 1)
            else:
                return False
        if len(stack) > 0:
            return False
        else:
            return True
