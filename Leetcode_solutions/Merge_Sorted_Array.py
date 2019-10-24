class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)):
            if nums1[i] == 0 and len(nums2) > 0:
                elem = nums2.pop()
                nums1[i] = elem
#         bubble sort
        for i in range(len(nums1) - 1, 0, -1):
            for j in range(len(nums1) - 1, 0, -1):
                if nums1[j - 1] > nums1[j]:
                    nums1[j - 1], nums1[j] = nums1[j], nums1[j - 1]
                else:
                    continue
        return nums1


2019-10-20T04:06:21.364213Z 1 [Note] A temporary password is generated for root@localhost: nP;!s/pXG29-
nP;!s/pXG29-