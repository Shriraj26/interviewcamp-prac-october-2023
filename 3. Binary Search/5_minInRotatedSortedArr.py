class Solution:
    def findMin(self, nums: List[int]) -> int:
        start,end = 0, len(nums) - 1
        right = nums[end]

        while start <= end :
            mid = start + (end - start)//2 
            if nums[mid] < right and( mid > 0 and nums[mid - 1] < nums[mid] ):
                end = mid - 1 
            elif nums[mid] > right :
                start = mid + 1 
            else :
                return nums[mid] 
 