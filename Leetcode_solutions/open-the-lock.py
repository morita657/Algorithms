import collections


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        dead_set = set(deadends)

        queue = collections.deque([('0000', 0)])
        visited = set('0000')

        while queue:
            (string, steps) = queue.popleft()
            # if the string is target return the steps
            if string == target:
                return steps
            # if the string is one of the dead_set, ignore it
            elif string in dead_set:
                continue

            for i in range(4):
                digit = int(string[i])
                for move in [-1, 1]:
                    new_digit = (digit + move) % 10
                    new_string = string[:i] + str(new_digit) + string[i + 1:]
                    # print string[:i], str(new_digit), string[i + 1:]
                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append((new_string, steps + 1))
        return -1


solution = Solution()
solution.openLock(["0201", "0101", "0102", "1212", "2002"],
                  "0202")
