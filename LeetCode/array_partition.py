class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        iterator = iter(nums)
        tupList = zip(iterator,iterator)
        return sum([min(i,j) for i,j in tupList])