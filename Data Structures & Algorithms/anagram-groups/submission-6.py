class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output_dict = {}
        for word in strs:
            freq_table = {}
            for letter in word:
                freq_table[letter] = freq_table.get(letter, 0) + 1
            key = str(sorted(freq_table.items()))
            output_dict[key] = output_dict.get(key, []) + [word]
        return list(output_dict.values())
             
            
        