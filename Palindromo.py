class Solution:
    def isPalindrome(self, x: int) -> bool:
        from copy import deepcopy 
        num = deepcopy(x)  
        
        if (x == 0):
            return True
        elif (x < 0) or (x % 10 == 0 ):
            return False
        
        rev = 0
        while (x != 0):
            pop = x % 10
            x //= 10
            
            rev = rev * 10 + pop
          
        return num == rev
           
        

n = Solution().isPalindrome(121)
print(n)
