from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # default dictionary(wont throw error if key doesn't exit, but will create it)
        # to hold the key which will be a count of the lowercase letters (convert list to tuple because dictionary can have a list as key)
        # and the values will be a list of the string that have the same occurrences of characters
            
        dictAnagrams = defaultdict(list)
        
        for anagram in strs:
            # list of a to z characters count
            characters = [0] * 26  
            for st in anagram:
                # characters can be from a to z
                # ord('a') = 
                characters[ ord(st) - ord('a')] += 1
            # add the key and value
            dictAnagrams[tuple(characters)].append(anagram)
            
        return dictAnagrams.values()
    
class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # default dictionary(wont throw error if key doesn't exit, but will create it)
        # to hold the key which will be a count of the lowercase letters (convert list to tuple because dictionary can have a list as key)
        # and the values will be a list of the string that have the same occurrences of characters
            
        dictAnagrams = {}
        
        for anagram in strs:
        #     # list of a to z characters count
            characters = [0] * 26  
            for st in anagram:
        #         # characters can be from a to za
        #         # ord('a') = a
                characters[ ord(st) - ord('a')] += 1
        #     # add the key and value
            dictAnagrams.setdefault(tuple(characters),[]).append(anagram)
            
        return dictAnagrams.values()   

        



strs = ["eat","tea","tan","ate","nat","bat"]



classA = Solution()
classB = Solution2()

print(classA.groupAnagrams(strs))
print(classB.groupAnagrams(strs))










