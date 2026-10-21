class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        longest_length = 0
        #Convert to set for o(1) access
        for i in nums:
            s.add(i)
        
        #Loop over set
        for x in s:
            if x-1 not in s:
                base = x
                length = 1
                while base + 1 in s:
                    length += 1
                    base += 1
                longest_length = max(longest_length, length)

        return longest_length


                    



        