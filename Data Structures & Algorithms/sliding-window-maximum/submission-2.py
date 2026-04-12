class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        for i in range(len(nums) - k + 1):
            currMax = nums[i]
            for j in range(i, i + k):
                if j-i > k:
                    continue
                
                currMax = max(nums[j], currMax)
            
            res.append(currMax)
        
        return res