class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numsSet = set(nums)
        # loop nums and check if the
        # number has a number one below it
        # if it does ignore it because it the
        # the beginning of the consecutive sequence
        # When we find the beginning of a set count
        # how many numbers occur after the start
        longest = 0
        
        for nu in nums:
            if not nu-1 in numsSet:
                long = 1
                value = nu + 1
                while value in numsSet:
                    value += 1
                    long += 1
                
                longest = max(longest, long)
                
                
        return longest
                
                


sol = Solution()
numbers = [1, 1, 2, 3, 900]


print(sol.longestConsecutive(numbers))

# numsSet = set(nums)

# longest = 0

# loop nums and check if the
# number has a number one below it
# if it does ignore it because it the
# the beginning of the consecutive sequence
# When we find the beginning of a set count
# how many numbers occur after the start

# for x in nums:
#     if (x-1) in numsSet:
#         pass  
#     else:
#         longestLoop = 1
#         val = x +1
#         while val in numsSet:
#             val += 1
#             longestLoop += 1
#         longest = max (longest, longestLoop)








