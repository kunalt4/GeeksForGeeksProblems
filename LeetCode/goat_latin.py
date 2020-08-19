class Solution:
    def toGoatLatin(self, S: str) -> str:
        i = 1
        vowels = set('AEIOUaeiou')
        S = S.split()
        for word in S:
            if word[0] not in vowels:
                word = word[1:] + word[0]
            word = word + "ma" + "a"*i
            S[i-1] = word
            i+=1
            
        return " ".join(S)
