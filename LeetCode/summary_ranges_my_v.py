class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        res = []
        
        while i < len(nums)-1:
            
            start = i
            
            while i < len(nums)-1 and nums[i+1] == nums[i] + 1:
                i+=1
            
            res.append(self.printRes(nums[start],nums[i]))
            i+=1
          
        if i == len(nums) - 1:
            res.append(self.printRes(nums[i],nums[i]))
        return res
    
    def printRes(self, start, end):
        if start == end:
            return str(start)
        else:
            return str(start) + "->"  + str(end)
