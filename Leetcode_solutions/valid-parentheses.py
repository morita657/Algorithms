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


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        patterns = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        if len(s) % 2 != 0:
            return False
        for i in range(len(s)):
            if s[i] in patterns.keys():
                stack.append(patterns[s[i]])
            else:
                if len(stack) == 0:
                    return False
                else:
                    remove = stack.pop()
                    if remove != s[i]:
                        return False
        if len(stack) == 0:
            return True


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
