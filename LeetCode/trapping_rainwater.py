class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        start = 0
        currArea = 0
        while height[start] < 1:
            start+=1
        end = start + 1
        while True:
            while end < len(height) and height[end] < height[start]:
                end+=1
                
            if end == len(height):
                end = start
                mylist = height[start+1:]
                if len(mylist) == 0:
                    break
                k = len(mylist) - mylist[::-1].index(max(mylist)) - 1
                for _ in range(k+1):
                    end+=1

            currArea += min(height[start],height[end])*(end-start)
            currArea = currArea - sum(height[start+1:end]) - min(height[start],height[end])
            
            start = end
            end = end + 1
        return currArea