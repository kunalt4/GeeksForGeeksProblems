class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            j = 0
            k = 0
            while(words[i][j]==words[i+1][k]):
                j+=1
                k+=1
                if j>=len(words[i]) or k>=len(words[i+1]):
                    break
            if(len(words[i+1])==k):
                return False
            if(order.index(words[i][j])>order.index(words[i+1][k])):
                return False
        return True
            
            