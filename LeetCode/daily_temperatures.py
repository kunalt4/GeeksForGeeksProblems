class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for i in range(len(T)-1):
            
            stack.append(i)            
            
            while stack and T[stack[-1]] < T[i+1]:
                node = stack.pop()
                val = i + 1 - node
                res[node] = val
            
        return res
