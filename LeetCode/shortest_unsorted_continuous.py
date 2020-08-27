class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        if len(nums) <= 1:
            return 0
        
        left = 0 
        right = len(nums) - 1
        
        while left < len(nums) - 1 and nums[left+1] >= nums[left]:
            left+=1
        
        while right > 0 and nums[right-1] <= nums[right]:
            right-=1
            
        if left > right:
            return 0
        
        mini = min(nums[left:right+1])
        maxi = max(nums[left:right+1])
        
        while left > 0 and mini < nums[left-1]:
            left-=1
        while right < len(nums) - 1 and maxi > nums[right+1]:
            right+=1
            
        return len(nums[left:right+1])
