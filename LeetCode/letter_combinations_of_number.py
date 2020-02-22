class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {"2":'abc',"3":'def',"4":'ghi',"5":'jkl',"6":'mno',"7":'pqrs',"8":'tuv',"9":'wxyz'}
        if digits == "":
            return []
        op = []
        for dig in digits:
            op.append(list(d[dig]))
        # for i in range(len(op)-1):
            
        res = ["".join(a) for a in list(itertools.product(*op))]
        return res
