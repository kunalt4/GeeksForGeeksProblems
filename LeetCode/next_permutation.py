class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def indexPeak(nums):
            i = len(nums) - 1
            while i>0 and nums[i] <= nums[i-1]:
                i-=1
            return i
        
        def reverseList(nums, start):
            end = len(nums) - 1
            while start<end:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end-=1
            
        
        pivot = indexPeak(nums) - 1

        if pivot == -1:
            nums.sort()
        else:
            
            i = len(nums) - 1
            while i>=0 and nums[i] <= nums[pivot]:
                i-=1
            nums[i], nums[pivot] = nums[pivot], nums[i]

            reverseList(nums, pivot+1)
            
            
# With some help from https://leetcode.com/problems/next-permutation/discuss/13994/Readable-code-without-confusing-ij-and-with-explanation
