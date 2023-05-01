class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :return type: List[int]
        """
        # O(n) time
        # O(1) space
    
        res = [1] * len(nums)
    
        prefix = 1
    
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
         
        postfix = 1
    
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix *= nums[i]
    
    # O(n*n)   this is a bad solution 
    # res = []       
    # for i, value in enumerate(nums):
    #     sum = 0
    #     status = True
    #     for j, value2 in enumerate(nums):
    #         if i != j: # we ignore i == j because this is the value being calculated
    #             if value2 == 0: # if any of the values is zero the resultant will be zero
    #                 sum = 0
    #                 break
                
    #             if status:
    #                 status = False
    #                 sum = value2
    #             else:
    #                 sum = sum * value2
    #     # set the return value            
    #     res.append(sum)
        
        return res
                    
test = [1,2,3,4]

sol = Solution()

print(sol.productExceptSelf(test))              