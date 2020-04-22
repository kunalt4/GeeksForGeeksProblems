class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.gen_par(n, n, "", result)
        return result
    
    def gen_par(self, left_rem, right_rem, path, result):
        if left_rem > right_rem or left_rem < 0 or right_rem < 0:
            return
        
        if right_rem == 0:
            result.append(path)
            return
            
        self.gen_par(left_rem-1, right_rem, path+"(", result)
        self.gen_par(left_rem, right_rem-1, path+")", result)
