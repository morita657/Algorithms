class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                if len(stack) < 2:
                    return False
                second = stack.pop()
                first = stack.pop()
                if token == "+":
                    result = first + second
                elif token == "-":
                    result = first - second
                elif token == "*":
                    result = first * second
                else:
                    if second == 0:
                        return False
                    result = abs(first) / abs(second)
                    if first * second < 0:
                        result = -result
                stack.append(result)
        if len(stack) != 1:
            return False
        return (stack[0])
