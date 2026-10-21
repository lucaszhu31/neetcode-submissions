class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        output, i  = [], 0
        # while not s: #inverted
        #     for i in range(len(s)):
        #         length = int(s[:i+1])
        #         if s[i+1] == "#" and length != 0:
        #             s = s[i+2:] #changing s here so ti dosent even work 
        #             output.append(s[i+2 : i+2+length])
        #             break
        #         elif len(s) == 2:
        #             output.append("")
        # return output 
      

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            output.append(s[j+1 : j+1 + length])
            i = j+1+length 
        return output 



    




