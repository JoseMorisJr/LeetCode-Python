
"""
Entregar una lista y un objetivo, y que se retorne una tupla con el índice de 
los dos números que suman esta lista. 
"""

class Solution:
    def twoSum(self, nums, target):
        x = 0
        for i , a in enumerate(nums):
            x += 1
            for j , b in enumerate(nums[x:]):
                if (a + b == target):
                    m = i 
                    n = j + x
                    break

            else:
                continue

            break
        return m , n



# a = Solution().twoSum([3,2,3],6)
# print(a)