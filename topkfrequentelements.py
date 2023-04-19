from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :return type: List[int]
        """

        # default dictionary with key number and value is the count
        # of the number

        #return a list of the k top values

        # count the occurrences of each number
        # and put in a dictionary
        dictNums = defaultdict(int)
        
        for i in nums:
            dictNums[i] += 1
            
        print(dictNums)
        
        # create a list of lists and the list index will be the count and the element
        # will be a list of numbers with that count , we are not using index 0
        count = [[] for i in range(len(nums) + 1 )]
        #count = [[]] * (len(nums) + 1)
        
        # populate the count list
        for i, v in dictNums.items():
            count[v].append(i)
        
        print(count)
        # return list of numbers
        ret = []
        
        # loop count from the end
        # the zero really be 1 because count[0] is not used.
        # but it shouldn't matter because we aren't using it.
        for v in range(len(count) -1, 0,-1):
            for n in count[v]:
                ret.append(n)
                if len(ret) == k:
                    return ret
             
                        


nums = [1,1,1,2,2,3]
k = 2
#Output: [1,2]

classSolution = Solution()

print(classSolution.topKFrequent(nums, k))

