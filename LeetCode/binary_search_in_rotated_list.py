class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return -1;
        
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = (start+end)//2
            
            if nums[mid] > nums[end]:
                if target > nums[mid] or target <= nums[end]:
                    start = mid+1
                else:
                    end = mid
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid+1
                else:
                    end = mid
            
            # if nums[start] == target:
                # return start
                    
        if nums[start] == target:
            return start
        
        return -1
