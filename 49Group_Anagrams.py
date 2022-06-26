#There's 2 main approaches to this problem
#Brute force Approach(Not shown)







#Hash Table Approach
#Time Complexity = O(n*m*logm) where m is the average length of the word
#Space Complexity = (O(n*m))

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        myDict = {}
        for word in strs:
            key = tuple(sorted(word))
            myDict[key] = myDict.get(key, []) + [words]
        return myDict.values()