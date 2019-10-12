class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        copy = target
        for i in range(len(numbers)):
            copy = target - numbers[i]
            for j in range(len(numbers)):
                if numbers[j] != numbers[i] and numbers[j] == copy:
                    return [i + 1, j + 1]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        copy = target
        ans = []
        while i < j:
            if numbers[i] + numbers[j] == target:
                ans = [i + 1, j + 1]
            if numbers[j] > target - numbers[i]:
                j -= 1
            else:
                i += 1
        return ans
