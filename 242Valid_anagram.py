#There's 2 main approaches to this problem
#Python Cheating approach -> return Counter(s) == Counter(t)


#Hash Table approach
#Time Complexity = O(s+t)
#Space Complexity = O(s+t)
#put charecters from each string into their 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if the length of the two strings is not the same, they cannot be anagrams
        if len(s)!=len(t):
            return False

        hashS,hashT = {},{}
        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i],0)
            hashT[s[i]] = 1 + hashT.get(t[i],0)

        for i in hashS:
            if hashS[i] != hashT.get(i,0):
                return False
        return True


#Sorting approach
#Time Complexity = O(n*logn)
#Space Complexity = O(n/1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
