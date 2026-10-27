class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #define output strucutre
        output_dict = defaultdict(list)

        #loop over words
        for word in strs:
            #standardized freq table 
            freq = [0] * 26
            for letter in word: 
                freq[ord(letter) - ord('a')] += 1
            output_dict[tuple(freq)].append(word)
        
        return list(output_dict.values())
            
            
            
        