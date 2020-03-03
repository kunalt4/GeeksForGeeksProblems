class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        candidates.sort()
        
        def combinationsSum(candidates,target,combinations,index=0,cur=[]):
            
            if target == 0:
                combinations.append(cur[:])
                

            # if index < len(candidates):
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                
                combinationsSum(candidates,target-candidates[i],combinations,i+1,cur+[candidates[i]])
                
        
        combinationsSum(candidates,target,combinations)
        return combinations

    
        