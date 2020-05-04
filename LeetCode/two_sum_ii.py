class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        temp = {}
        for i,n in enumerate(numbers):
            sec = target-n
            if sec in temp:
                return [temp[sec]+1,i+1]
            else:
                temp[n] = i
