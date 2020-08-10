# Using the approach here -- https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/discuss/14707/9-11-lines-O(log-n)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binSearch(n):
            low = 0
            high = len(nums)
            
            while low < high:
                
                mid = (low+high)//2
                
                if nums[mid]>=n:
                    high = mid
                else:
                    low = mid + 1
                    
            return low
        
        low = binSearch(target)
        if target in nums[low:low+1]:
            return [low, binSearch(target+1)-1]
        else:
            return [-1,-1]
