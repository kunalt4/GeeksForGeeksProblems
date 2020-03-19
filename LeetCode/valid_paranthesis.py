class Solution:
    def isValid(self, s: str) -> bool:
        paran_dict = {')':'(','}':'{',']':'['}
        stack_p = []
        for c in s:
            if c in paran_dict.values():
                stack_p.append(c)
                
            elif c in paran_dict.keys():
                if stack_p == [] or paran_dict[c] != stack_p.pop():
                    return False
            else:
                return False
        return stack_p == []
                    
