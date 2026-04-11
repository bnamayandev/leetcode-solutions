class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i+1, len(nums) - 1

            while l < r:
                threeSum = nums[l] + nums[r] + nums[i]
                if threeSum > 0:
                    r -= 1
                
                elif threeSum < 0:
                    l += 1
                else:
                    res.add((nums[l], nums[r], nums[i]))
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return [list(t) for t in res]