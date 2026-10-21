class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = defaultdict(int)
        # for num in nums: 
        #     freq[num] += 1
        
        # max_values = sorted(freq.values())[-k:]
        
        # keys = [k for k, v in freq.items() if v in max_values]
        # return keys 
        freq = defaultdict(int)
        output = []
        for num in nums:
            freq[num] += 1

        buckets = [[] for _ in range(0,len(nums)+1)]
        
        for value, count in freq.items():
            buckets[count].append(value)
        
        output = []
        for values in reversed(buckets):
            if not values:
                continue
            for value in values:
                output.append(value)
            if len(output) == k:
                return output
        

        

        
        


    
            


        