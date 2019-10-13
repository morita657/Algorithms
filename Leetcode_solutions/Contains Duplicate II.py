class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memory = collections.defaultdict(list)
        for i in range(len(nums)):
            memory[nums[i]].append(i)
        for index, key in enumerate(memory):
            if len(memory[key]) >= 2:
                for j in range(1, len(memory[key])):
                    if memory[key][j] - memory[key][j - 1] <= k:
                        return True
        return False
