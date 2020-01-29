class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d = {}
        for c in range(len(s)):
            
            if s[c] not in d:
                if t[c] not in d.values():
                    d[s[c]] = t[c]
                else:
                    return False
            
            elif d[s[c]]!=t[c]:
                return False
            else:
                continue
        
        return True
