class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_str = ""
        allowed_char = set("abcdefghijklmnopqrstuvwxyz0123456789")
        for char in s.lower():
            if char in allowed_char:
                filtered_str += char

        for i in range(0,len(filtered_str)//2):
            j = -i-1
            if filtered_str[i] != filtered_str[j]:
                return False
        return True 

        #1st mistake, capital letters

        