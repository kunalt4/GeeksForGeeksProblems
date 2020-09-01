class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_prod = nums[0]
        min_prod = nums[0]
        ans = nums[0]
        
        #Max product could be curr_max * curr_num or for negatives, curr_min * curr_num
        
        
        for i in range(1,len(nums)):
            x = max(nums[i], max_prod*nums[i], min_prod*nums[i]) #Calculate max upto current point
            min_prod = min(nums[i], max_prod*nums[i], min_prod*nums[i]) #Calculate min upto current point
            max_prod = x
            ans = max(max_prod, ans)
        
        return ans
