import random

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        for rect in rects:
            area = (rect[2]-rect[0]+1)*(rect[3]-rect[1]+1)
            self.weights.append(area)
        
        sum_weights = sum(self.weights)
        self.weights = [x/sum_weights for x in self.weights]

    def pick(self) -> List[int]:
        rect = random.choices(population=self.rects, weights=self.weights, k=1)[0]
        return [random.randint(rect[0], rect[2]), random.randint(rect[1],rect[3])]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

#With help from this explanation https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/discuss/805335/Python-readable-commented-solution-without-using-bisect
