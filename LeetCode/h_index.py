class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        for c in range(n):
            if citations[c] >= (n - c):
                return (n-c)
        return 0
