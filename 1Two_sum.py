#There's two approaches to this problem
#There's the brute force approach
#There's the hash table approach
#Time Complexity = O(n^2)
#Space Complexity = (O(1))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    if nums[i]+nums[j]==target:
                        return i,j
                    else:
                        continue


#Hash Table approach
#Time Complexity = O(n)
#Space Complexity = (O(n))
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Visitedmap = {}# contains Value -> index
        for i,n in enumerate(nums):
            diff = target - n
            if diff in Visitedmap:
                return[Visitedmap[diff],i]
            Visitedmap[n]=i