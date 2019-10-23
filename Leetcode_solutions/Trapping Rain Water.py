
class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        for i in range(len(height)):
            max_left=0
            max_right=0
            for j in range(len(height)):
                max_left=max(max_left,height[i])
                max_right=max(max_right,height[i])
            ans+=min(max_left,max_right)
        return ans