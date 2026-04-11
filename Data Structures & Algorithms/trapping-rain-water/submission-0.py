class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = [height[0]] * len(height)
        rightMax = [height[-1]] * len(height)

        for i in range(1, len(height)):
            leftMax[i] = max(leftMax[i-1], height[i])
            rightMax[-i - 1] = max(rightMax[-i], height[-i - 1])
        
        res = 0
        for i in range(len(height)):
            res += (min(leftMax[i], rightMax[i])) - height[i]
        
        return res
        