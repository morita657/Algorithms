class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        q = []
        for i in range(len(nums)):
            q.append((nums[i], i))
        counts = []
        count = 0
        while len(q) > 0:
            now = q.pop(0)
            elem, index = now[0], now[1]
            crange = nums[index + 1:]
            for j in range(len(crange)):
                if crange[j] < elem:
                    count += 1
            counts.append(count)
            count = 0
        return counts
