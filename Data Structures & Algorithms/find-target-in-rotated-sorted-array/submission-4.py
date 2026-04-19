class Solution:
    def search(self, nums: List[int], t: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: 
            m = (l + r) // 2

            if nums[m] == t:
                return m
            
            if nums[l] <= nums[m]:
                if t > nums[m] or t < nums[l]:
                    l = m + 1
                
                else:
                    r = m - 1
            
            else:
                if t < nums[m] or t > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        
        return -1
        