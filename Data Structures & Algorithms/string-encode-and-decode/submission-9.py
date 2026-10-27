class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for word in strs:
            encoded_string += str(len(word)) + "#" + word
        return encoded_string
   

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i <= len(s) - 1:
            length = ""
            while s[i].isdigit():
                length += s[i]
                i += 1
            decoded_strs.append(s[i+1: i+1 + int(length)])
            i += int(length) + 1

        return decoded_strs



 



    




