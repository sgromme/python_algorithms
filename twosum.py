from collections import defaultdict

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create dictionary, with the key as the original sort of the list, and sort
        hashmap = {}
        for i, value in enumerate(nums):
            
            difference = target-value
            if difference in hashmap:
                return [ hashmap[difference], i]
            # add value to hashmap
            hashmap[value] = i
       
        return 


a = [2, 15, 11, 7]
a_target = 9






s = Solution()

print(s.twoSum(a,a_target))
















