class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        res = [0] * len(nums)

        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
            suffix[-i-1] = suffix[-i] * nums[-i-1]
        
        print(prefix)
        print(suffix)
        
        for i in range(len(nums)):
            if i == 0:
                res[i] = suffix[1]
            
            elif i == len(nums) - 1:
                res[i] = prefix[len(nums) - 2]
            
            else:
                res[i] = prefix[i - 1] * suffix[i + 1]

        return res