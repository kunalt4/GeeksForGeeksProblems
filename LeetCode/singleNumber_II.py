class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for i in range(0,len(nums)-3,3):
            if nums[i]!=nums[i+1]:
                return nums[i]
        return nums[-1]