class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        nums1ptr = m
        nums2ptr = 0

        while nums1ptr < len(nums1):
            nums1[nums1ptr] = nums2[nums2ptr]
            nums1ptr += 1
            nums2ptr += 1
        
        nums1.sort()