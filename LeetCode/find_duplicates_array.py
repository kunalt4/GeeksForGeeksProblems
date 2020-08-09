class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if nums[abs(num)-1]<0: #check whether the value in the index corresponding to the number is negative
                res.append(abs(num))
            else:
                nums[abs(num)-1]*=-1
        return res
