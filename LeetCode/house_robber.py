class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        
        if len(nums) <=2:
            return max(nums)
        
        rob = [0] * (len(nums) + 1)
        
        rob[0] = 0
        rob[1] = nums[0]
        
        for i in range(1, len(nums)):
            rob[i+1] = max(rob[i-1]+nums[i], rob[i])
            
        return rob[-1]
    
