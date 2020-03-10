class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        eles = {}
        for num in nums:
            if num in eles:
                eles[num]+=1
            else:
                eles[num]=1
        return [k for k,v in eles.items() if v>len(nums)//2][0]