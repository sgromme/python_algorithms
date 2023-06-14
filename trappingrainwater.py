from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max = height[0]
        right_max = height[len(height)-1]
        left_pointer = 0
        right_pointer = len(height) - 1
        volume = 0
        # formula
        # volumne[i] = min(leftmax, height[i]) - current height[i]
        # 
        
        # if the height is empty (len(height) =  0)
        if not height: return 0
        
        while left_pointer < right_pointer:
            
            if left_max < right_max:
                left_pointer += 1
                left_max = max(left_max, height[left_pointer])
                volume += left_max - height[left_pointer]
            else:
                right_pointer -= 1
                right_max = max(right_max, height[right_pointer])
                volume += right_max - height[right_pointer]
                
        return volume
            
       
    



height = [0,1,0,2,1,0,1,3,2,1,2,1]  # answer is 6

# iterate the list and ever the current value (initialize current value to 0) is greater than the previous
# value store this value and if the next value is equal or greater  subtract these
# to get the storage.



sol = Solution()

print(sol.trap(height))