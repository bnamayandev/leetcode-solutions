class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targets = {} # value -> index

        for i,n in enumerate(nums):
            if target - n in targets:
                return [targets[target - n], i]
            
            else:
                targets[n] = i