class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 
            m = l + ((r - l) // 2)

            if nums[m] == t:
                return m
            
            if (t >= nums[m] >= nums[r]) or (nums[r] >= t >= nums[m]) or (t <= nums[r] <= nums[m]):
                l = m + 1
            
            else:
                r = m - 1

        
        return -1
        