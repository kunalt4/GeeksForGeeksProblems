class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower():
            return True
        
        if word[0].isupper():
            if any(x.isupper() for x in word[1:]):
                return False
            return True
        else:
            return False
            
