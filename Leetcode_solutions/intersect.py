class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        resume = 0
        small = []
        big = []
        if len(nums1) > len(nums2):
            small = nums2
            big = nums1
        else:
            small = nums1
            big = nums2
        for i in range(len(small)):
            for j in range(len(big)):
                if small[i] == big[j]:
                    ans.append(small[i])
                    big.pop(big.index(small[i]))
                    break
        return ans
