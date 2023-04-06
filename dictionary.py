# examples of dictionarys

import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        #return Counter(s) == Counter(t)
        
        
    
    
    
        
        

s1 = {'a':1, 'b':5}

s2 = {'b':5, 'a':1}

print(collections.Counter(s1))

print(collections.Counter(s1)==collections.Counter(s2))


