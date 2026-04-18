class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        has = set()

        for num in nums:
            if num in has:
                return num
            
            has.add(num)
        