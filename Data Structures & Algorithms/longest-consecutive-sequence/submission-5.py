class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        output = 0 
        for num in nums:
            if num - 1 in nums:
                continue
            else:
                consecutive_len = 1
                next_num = num + 1
                while next_num in nums:
                    consecutive_len += 1
                    next_num += 1
                output = max(output, consecutive_len)

        return output 
                
                    




#o(2n) max => (o(N))
      
                    



        