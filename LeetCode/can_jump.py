class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) < 2:
            return True
        
        target = len(nums) - 1
        step = 0
        i = 0
        
        while i <= step:
            
            if nums[i]+i>step:
                step = nums[i] + i
                
            i+=1
            
            if step >= target:
                return True
            
        return False
