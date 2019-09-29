class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = collections.defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += 1
        ans = []
        for index, key in enumerate(d):
            if d[key] > len(nums) // 3:
                ans.append(key)
        return list(set(ans))
