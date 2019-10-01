class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) == 0:
            return -1
        ans = None
        mid = len(A) // 2
        if A[mid - 1] >= A[mid]:
            while A[mid - 1] >= A[mid]:
                mid -= 1
            return mid
#             iterate left side

        elif A[mid + 1] >= A[mid]:
            while A[mid + 1] >= A[mid]:
                mid += 1
            return mid
#         iterate right side
        else:
            return mid


class Solution(object):
    def peakIndexInMountainArray(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = (lo + hi) / 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
