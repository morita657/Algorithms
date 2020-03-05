# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            for i in range(n + 1):
                if isBadVersion(i):
                    return i
        else:
            return self.bs(0, n)

    def bs(self, start, end):
        if end - start < 10:
            for i in range(start, end + 1):
                if isBadVersion(i):
                    return i
        else:
            mid = (end - start) // 2 + start
            if isBadVersion(mid):
                return self.bs(start, mid)
            else:
                return self.bs(mid + 1, end)
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        while start < end:
            mid = (end - start) // 2 + start
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return -1
        left = 1
        right = n
        while left < right:
            mid = (left + right)//2
            if isBadVersion(mid) and isBadVersion(mid-1)==False:
                return mid
            elif isBadVersion(mid) and isBadVersion(mid-1)==True:
                right = mid
            else:
                left = mid+1
        if left ==right and isBadVersion(left):
            return left
        return -1