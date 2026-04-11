class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has = set()

        for n in nums:
            if n not in has:
                has.add(n)
            else:
                return True
        return False

        