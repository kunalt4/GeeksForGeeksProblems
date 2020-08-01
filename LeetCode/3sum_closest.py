class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        curMin = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            
            left, right = i+1, len(nums)-1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == target:
                    return total
                
                if abs(total-target) < abs(curMin-target):
                    curMin = total
                
                if total < target:
                    left+=1
                else:
                    right-=1
            
        return curMin
    
