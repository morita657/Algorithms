class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            sum = 0
            for end in range(i, len(nums)):
                sum += nums[end]
                if sum == k:
                    ans += 1
        return ans


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for start in range(len(nums)):
            total = 0
            for end in range(start, len(nums)):
                total += nums[end]
                if total == k:
                    count += 1
        return count


public class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0, sum = 0
        HashMap < Integer, Integer > map = new HashMap < > ()
        map.put(0, 1)
        for (int i=0
             i < nums.length
             i + +) {
            sum += nums[i]
            if (map.containsKey(sum - k))
            count += map.get(sum - k)
            map.put(sum, map.getOrDefault(sum, 0) + 1)
        }
        return count
    }
}


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        preSum, ret, size = [0], 0, len(nums)
        count = collections.Counter(preSum)
        if size == 1:
            return 1 if nums[0] == k else 0
        for val in nums:
            s = preSum[-1] + val
            preSum.append(s)
            ret += count.get(s - k, 0)
            count[s] = count.get(s, 0) + 1

        return ret
