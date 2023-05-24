class Solution():
    
    
    
    def encode(self, strs):
        """
    :type str: List(string)
    :return type: string
    
    """ 
        temp = ""
        for val in strs:
            temp += str(len(val)) + "#" + val
        return temp
    
    
    def decode(self, str):
        """
        :type str: string
        :return type List(str)
        """ 
        ret = []
        i = 0
        j = 0
        while i < len(str):
            if str[i] == "#":
                length = int(str[j:i])
                ret.append(str[i + 1: i + 1 + length])
                i = i + 1 + length
                j = i
            i += 1
        return ret
    
    

class Solution2:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        pass

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        pass

#Input: ["we", "say", ":", "yes"]
#Output: ["we", "say", ":", "yes"]

#Input: ["lint","code","love","you"]
#Output: ["lint","code","love","you"]


       
s = ["test","bubba", "#4testssdf"]

classSolution = Solution()
print(classSolution.encode(s))

r = classSolution.encode(s)

print(classSolution.decode(r))







