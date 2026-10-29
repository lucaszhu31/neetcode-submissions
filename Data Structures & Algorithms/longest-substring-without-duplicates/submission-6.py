class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = l = 0
        dups = {}
        for i, char in enumerate(s):
            if char in dups:
                l = max(dups[char] + 1, l)
            dups[char] = i
            best = max(best, i - l + 1) 
        
        return best
