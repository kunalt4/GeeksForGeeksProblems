class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = frozenset(["a","e","i","o","u","A","E","I","O","U"])
        vowels_list = []
        for c in s:
            if c in vowels:
                vowels_list.append(c)
        
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowels_list.pop()
                
        return "".join(s)
                