class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = 0
        result = []
        while i < len(nums)-1:
            if nums[i]!=nums[i+1]:
                result.append(nums[i])
                i+=1
            else:
                i+=2
            if len(result) == 2:
                return result
        
        return result+[nums[-1]] if len(result)==1 else nums[-2:]
            