class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos = None
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            elif nums[0] < target:
                return 1
            else:
                return 0
        else:
            for i in range(1, len(nums)):
                if nums[i] == target:
                    pos = i
                    break
                elif nums[i - 1] < target and nums[i] > target:
                    pos = i
                    break
                elif i == len(nums) - 1 and target > nums[i]:
                    pos = i + 1
                else:
                    pos = 0
            return pos
