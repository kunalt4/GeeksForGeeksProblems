class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_loc = 0
        one_loc = 0
        two_loc = len(nums)-1
        
       
        
        while one_loc <= two_loc:
            
            if nums[one_loc] == 0:
                nums[one_loc], nums[zero_loc] = nums[zero_loc], nums[one_loc]
                zero_loc += 1
                one_loc+=1
            elif nums[one_loc] == 2:
                nums[one_loc], nums[two_loc] = nums[two_loc], nums[one_loc]
                two_loc -=1
            else:
                one_loc+=1
