class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        
        trie = self.trie
        for w in word:
            if w not in trie:
                trie[w] = {}
            trie = trie[w]
        trie['#'] = '#'
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self._searchDFS(word, self.trie)
        
    def _searchDFS(self, word, trie):
        
        for i,w in enumerate(word):
            
            if w=='.':
                return (any(self._searchDFS(word[i+1:], trie[c]) for c in trie if c != '#'))
            if w not in trie:
                return False
            trie = trie[w]
        return '#' in trie
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
