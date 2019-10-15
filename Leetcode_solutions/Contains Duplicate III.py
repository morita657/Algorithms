# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if abs(nums[i] - nums[j]) <= t and abs(j - i) <= k:
#                     return True
# return False


# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums, k, t):
#         i = 0
#         j = 1
#         while i < j and j < len(nums):
#             condition = abs(nums[i] - nums[j]) <= t and abs(i - j) <= k
#             if condition:
#                 return True
#             while not condition and i < j:
#                 if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
#                     return True
#                 i += 1
#             i = 0
#             j += 1
#         return False

from collections import OrderedDict


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
            return False
        dic = OrderedDict()
        for n in nums:
            key = n if not t else n // t
            for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = n
        return False


class Solution:
    def containsNearbyAlmostDuplicate(self, A, k, t):
        n = len(A)

        A = list(zip(A, range(n)))
        A.sort()

        for i in range(n):
            j = i + 1
            while j < n and A[j][0] - A[i][0] <= t:
                if abs(A[j][1] - A[i][1]) <= k:
                    return True
                else:
                    j += 1

        return False


s = Solution()
# s.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
s.containsNearbyAlmostDuplicate([7, 1, 3], 2, 3)
