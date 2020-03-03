class Solution:
    
    def combinationSum(self, candidates: List[int], target: int, index=0, cur=[]) -> List[List[int]]:
        
        def combinationsSum(candidate,target,combinations=[],index=0,cur=[]):
            
            if target == 0:
                combinations.append(cur[:])
                
            if target <= 0:
                return

            if index < len(candidates):

                value = candidates[index]
                cur.append(value)
                combinationsSum(candidates,target-value,combinations,index,cur)
                cur.pop()
                combinationsSum(candidates,target,combinations,index+1,cur)
                
            return combinations
        
        return combinationsSum(candidates,target)
        
        