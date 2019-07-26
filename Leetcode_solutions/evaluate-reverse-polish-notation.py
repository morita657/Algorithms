import operator
import math


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums = []
        result = 0
        # etc.
        ops = {"+": operator.add, "-": operator.sub,
               "*": operator.mul, "/": operator.div}
# print ops["+"](1,1)
        for elem in tokens:
            if elem.isdigit():
                print 'elem: ', int(elem)
                nums.append(int(elem))
            else:
                print nums
                res = ops[elem](nums[len(nums) - 2], nums[len(nums) - 1])
                res = math.floor(res)
                # print nums[len(nums) - 1] 5
                nums.pop(len(nums) - 1)
                # print nums[len(nums) - 2] 4
                nums.pop(len(nums) - 1)
                nums.append(res)
        return int(nums[0])


["2", "1", "+", "3", "*"]
["4", "13", "5", "/", "+"]
["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
