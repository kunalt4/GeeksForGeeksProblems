class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = {}
        result = []
        
        for num in nums1:
            counts[num] = counts.get(num,0)+1
        
        for num in nums2:
            if num in counts and counts[num]>0:
                result.append(num)
                counts[num]-=1
        return result
