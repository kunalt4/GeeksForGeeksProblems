class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            while nums[i]-1 >= 0 and nums[i]-1 < n and nums[nums[i]-1]!=nums[i]:
                tmp = nums[i]-1
                nums[i], nums[tmp] = nums[tmp], nums[i]
         
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
# Help from https://leetcode.com/problems/first-missing-positive/discuss/17161/Python-O(n)-and-O(nlgn)-solutions.
