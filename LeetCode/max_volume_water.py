class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxVol = 0
        width = len(height) - 1
        left = 0
        right = len(height) - 1
        for w in range(width,0,-1):
            if height[left] > height[right]:
                maxVol = max(maxVol, height[right]*w)
                right = right - 1
            else:
                maxVol = max(maxVol, height[left]*w)
                left = left + 1
        return maxVol