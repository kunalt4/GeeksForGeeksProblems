class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        for i, let in enumerate(zip(*strs)):
            if len(set(let)) > 1:
                return strs[0][:i]
        return min(strs)
