class Solution:

    def canJumpFromPosition(self, position, nums):
        if position == len(nums) - 1:
            return True
        furthestJump = min(position + nums[position], len(nums) - 1)
        for nextPosition in range(position + 1, furthestJump + 1):
            if self.canJumpFromPosition(nextPosition, nums):
                return True
        return False

    def canJump(self, nums: List[int]) -> bool:
        return self.canJumpFromPosition(0, nums)


class Solution:

    def canJumpFromPosition(self, position, nums):
        if position == len(nums) - 1:
            return True
        furthestJump = min(position + nums[position], len(nums) - 1)
        # for nextPosition in range(position + 1, furthestJump + 1):
        for nextPosition in range(furthestJump, position, -1):
            if self.canJumpFromPosition(nextPosition, nums):
                return True
        return False

    def canJump(self, nums: List[int]) -> bool:
        return self.canJumpFromPosition(0, nums)


class Solution:

    def canJumpFromPosition(self, position, nums):
        if self.memo[position] != "U":
            return True if self.memo[position] == 'G' else False

        furthestJump = min(position + nums[position], len(nums) - 1)
        for nextPosition in range(position + 1, furthestJump + 1):
            if self.canJumpFromPosition(nextPosition, nums):
                self.memo[position] = "G"
                return True
        self.memo[position] = "B"
        return False

    def canJump(self, nums: List[int]) -> bool:
        self.memo = ["U" for i in range(len(nums))]
        self.memo[len(self.memo) - 1] = 'G'
        return self.canJumpFromPosition(0, nums)


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        self.memo = ["U" for i in range(len(nums))]
        self.memo[len(self.memo) - 1] = 'G'

        for i in range(len(nums) - 2, -1, -1):
            furthestJump = min(i + nums[i], len(nums) - 1)
            for j in range(i + 1, furthestJump + 1):
                if self.memo[j] == "G":
                    self.memo[i] = "G"
                    break
        return self.memo[0] == "G"


class Solution:

    def canJump(self, nums):
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0


s = Solution()
s.canJump([9, 4, 2, 1, 0, 2, 0])
