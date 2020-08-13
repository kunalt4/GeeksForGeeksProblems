class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.c = characters
        self.len = combinationLength
        self.cur = ""

    def next(self) -> str:
        if self.cur == "":
            self.cur = self.c[:self.len]
        else:
            end = 0
            while end < len(self.cur): #getting the common suffix point, or the place we can update
                if self.cur[::-1][end] == self.c[::-1][end]:
                    end+=1
                else:
                    break
            location = self.c.index(self.cur[-end-1])
            self.cur = self.cur[:-end-1]+self.c[location+1:location+2+end]
            print(end, location)
        return self.cur

    def hasNext(self) -> bool:
        return self.cur != self.c[-self.len:]

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()


#Help from https://leetcode.com/problems/iterator-for-combination/discuss/790113/Python-O(k)-on-the-fly-explained
