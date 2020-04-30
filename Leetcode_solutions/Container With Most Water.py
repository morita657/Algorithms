class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            currentArea = (right - left) * min(height[left], height[right])
            # print(area,currentArea)
            if area < currentArea:
                area = currentArea
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
# brute force
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                total = min(height[i], height[j]) * (j - i)
                ans = max(total, ans)
        return ans
                

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        l = 0
        r = len(height) - 1
        while l < r:
            maxarea = max(maxarea, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxarea