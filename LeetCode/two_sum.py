class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i,n in enumerate(nums):
            sec = target-n
            if sec in temp:
                return [temp[sec],i]
            else:
                temp[n] = i
