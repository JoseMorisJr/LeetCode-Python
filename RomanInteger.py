"""
Codigo no creado por mi
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        
        dict_romano =  {"I":1 , "V":5, "X":10, "L": 50, "C":100, "D": 500, "M":1000}
        
        num = 0
        i = 0
        
        while i < len(s) - 1:
            if dict_romano[s[i]] >= dict_romano[s[i+1]]:
                num += dict_romano[s[i]]
                i+=1
            else:
                num += dict_romano[s[i+1]] - dict_romano[s[i]] 
                i+=2
                
        if i < len(s): 
            num += dict_romano[s[i]]
            
        return num
            
n = Solution().romanToInt("XXIX")
print(n)