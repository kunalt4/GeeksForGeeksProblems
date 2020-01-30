class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for char in range(1,len(nums)):
            if nums[i] != nums[char]:
                i+=1
            nums[i] = nums[char]
        return i+1
