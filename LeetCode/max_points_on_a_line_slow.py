from collections import Counter
from fractions import Fraction
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        
        maximum_val = 0
        
        for p in points:
            slope_dict = {}
            cur_max = 0
            duplicate = 0
            for q in points:
                if p!=q:
                    if p[0] == q[0]:
                        slope = 'inf'
                    else:
                        slope = Fraction((q[1]-p[1]),(q[0]-p[0]))
                    
                    slope_dict[slope] = slope_dict.get(slope,0)+1
                    cur_max = max(cur_max, slope_dict[slope])
                else:
                    duplicate += 1
            maximum_val = max(maximum_val, duplicate+cur_max)
            
        return maximum_val