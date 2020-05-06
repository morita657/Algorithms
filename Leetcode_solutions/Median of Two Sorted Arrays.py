class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joinedList = nums1 + nums2
        joinedList.sort()
        if len(joinedList)%2==0:
            median = len(joinedList)//2
            return (joinedList[median-1]+joinedList[median])/2
        else:
            median = len(joinedList)//2
            return joinedList[median]