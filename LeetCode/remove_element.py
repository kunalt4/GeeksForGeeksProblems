class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums) - 1
        i = 0
        
        while i <= n:
            while nums[n] == val:
                n-=1
                if i>n:
                    del nums[i:]
                    return len(nums)
            if nums[i] == val:
                nums[i], nums[n] = nums[n], nums[i]
                n-=1
            i+=1
            
        del nums[n+1:]
        return len(nums)
