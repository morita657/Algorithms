class Solution:
    def countAndSay(self, n: int) -> str:
        ans = ['1', '11', '21']
        index = 2
        if n < 3:
            return ans[n - 1]
        while index != n - 1:
            current = ans[-1]
            count = 1
            element = ""
            for i in range(1, len(current)):
                if current[i] != current[i - 1]:
                    element += str(count) + current[i - 1]
                    count = 1
                else:
                    count += 1
            element += str(count) + current[i]
            ans.append(element)
            index += 1
        return ans[n - 1]
