class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = collections.Counter(nums)
        ls = sorted(nums,key= lambda x: (counter[x],x),reverse=True)
        i = 0 
        dict = {}
        while len(dict)!=k:
            dict[ls[i]] = 1
            i+=1
        return list(dict.keys())