 '''Example : pwwp '''
    # seen ={}, left= 0, curr_max =0
    
    # Loop first : index = 0, letter = p ,left = 0 first if --> false (no value in seen yet) curr_max = max(0, 0-0+1) --> 1 --> This covers the case for string with single character case. --> seen ={'p':0} 
    
    # Loop second: index = 1, letter = w, left = 0,seen = {'p' : 0} first condition -->false (w not in seen). so curr_max = max(1, 1-0+1) = 2.
    
    # Loop third: seen = {'p':0, 'w' : 1}, letter= 'w' first condition --> true (w is in seen and left = 0 <= seen['w'] =1). So set, left = seen['w'] + 1 = 2, seen['w'] = index = 2, seen = {'p': 0, w:'2'} 
    
    # Loop fourth: seen = {'p': 0, 'w' : 2}, letter = 'p', curr_max = 2, index=3, first_condition --> false (left = 2 , seen['p']= 0, so 2<=0 is false). curr_max = max(2,3-2+1) = 2. Giving same curr_max again.
    
    # Max computed
    
    #Algorithm: 
    
   '''  
    # Start from the beginning of the string
    # See if the current visiting letter has already been visited or not. 
    # If it has been visited previously then its a duplicate. To make sure we are marking the most recent letter, we store only the index of the most recent letter for the duplicates letter in the seen.
    # If you encounter a duplicate but your current left position is greater than the duplicate index then ignore it. and update the index of the duplicate letter. Else start from the right of the previous index of duplicate 
    # Every time, you don't see any duplicates, compute the max and check with the current max.
    # Return the max computed '''
 
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        curr_max = 0 
        for index, letter in enumerate(s):
            if letter in seen and left <= seen[letter]:
                left = seen[letter] + 1   
            else:
                curr_max = max(curr_max, index - left + 1)
            seen[letter] = index


        return curr_max
        