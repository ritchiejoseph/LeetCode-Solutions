#There's three approaches to this problem
#The brute force approach(a linear search)
#The Binary Search approach
#The Binary Search approach but only on the even indices


#The brute force approach(a linear search)
#Time Complexity = O(n)
#Space Complexity = (O(1))
def singleNonDuplicate(self, nums: List[int]) -> int:
    for i in range(0, len(nums) - 2, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]
    return nums[-1]


#The Binary Search approach
#Time Complexity = O(log(n))
#Space Complexity = (O(1))
def singleNonDuplicate(self, nums: List[int]) -> int:
    lo = 0
    hi = len(nums) - 1   
    while lo < hi:
        mid = lo + (hi - lo) // 2
        halves_are_even = (hi - mid) % 2 == 0
        if nums[mid + 1] == nums[mid]:
            if halves_are_even:
                lo = mid + 2
            else:
                hi = mid - 1
        elif nums[mid - 1] == nums[mid]:
            if halves_are_even:
                hi = mid - 2
            else:
                lo = mid + 1
        else:
            return nums[mid]
    return nums[lo]



#The Binary Search approach but only on the even indices
#Time Complexity = O(log(n))
#Space Complexity = (O(1))
#although this approach does not directly imporove on the time complexity from 
#the previous approach, it is a more elegant and easy to explain solution
def singleNonDuplicate(self, nums: List[int]) -> int:
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            lo = mid + 2
        else:
            hi = mid
    return nums[lo]