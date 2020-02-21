class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p = "".join(sorted(p))
        p_len = len(p)
        print(p)
        print(p_len)
        for i in range(len(s)-p_len+1):
            if "".join(sorted(s[i:i+p_len])) == p:
                res.append(i)
        return res
