class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if not nums: return []
        i = 0
        res = []
        start = 0
        while i < len(nums)-1:
            
            if nums[i+1] != nums[i] + 1:
                res.append(self.printRes(nums[start],nums[i]))
                start = i + 1
            i+=1
            
        res.append(self.printRes(nums[start],nums[i]))
        return res
    
    def printRes(self, start, end):
        if start == end:
            return str(start)
        else:
            return str(start) + "->"  + str(end)
