class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        l = r = best = 0

        while r <= len(s) - 1:
            length = r - l + 1 
            freq[s[r]] += 1
            max_freq = max(freq.values())

            if length - max_freq <= k:
                best = max(best, length)
                r += 1
            elif length - max_freq > k:
                freq[s[l]] -= 1
                freq[s[r]] -= 1
                l += 1
        
        return best


        