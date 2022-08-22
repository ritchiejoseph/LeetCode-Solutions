nums = [1,2,3,4,5,5,6]
#There's four primary approaches to this problem
#There's the brute force approach
#There's the hash table approach
#There's the sorting approach
#There's the python sets approach

#Brute Force Approach
#Time Complexity = O(n^2)
#Space Complexity = (O(1))
#Compare Every number to every other number in the array

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False


#Hash Table Approach
#Time Complexity = O(n)
#Space Complexity = (O(n))

#Essentially checks if number is already in the Hash Table, if it is, returns True
#If not in the hash table adds the element to the hash table, 
#If the program runs through the entire array and does not find a duplicate, returns False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i in nums:
            if i not in hashMap:
                hashMap[i] = 1
            else:
                return True
        return False

#Sorting Approach
#Time Complexity = O(n*logn)
#Space Complexity = (O(1))

#Sorts the array, and then checks adjacent elements for equality, 
#If it does find equal adjacent elements, returns True, else Returns False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Checking for the case where the array is either empty or has only 1 element
        if len(nums)<2:
            return False
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


#Python sets approach
#Time Complexity = O(?)
#Space Complexity = (O(n))

#Python has a data structure called sets
#Sets is essentially a data structure similar to an array, except, it does not allow duplicates
#We can use this property of sets to easily solve this question, since if the input array did have any duplicates
#the length of the array would be different from the length of the set of the numbers in the array

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return not(len(set(nums)) == len(nums))
