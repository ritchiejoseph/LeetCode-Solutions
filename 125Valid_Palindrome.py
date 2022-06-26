# class Solution:
#     def isPalindrome(self, s: str) -> bool:

s = "A man, a plan, a canal: Panama"
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = [i for i in s.lower() if i.isalnum()]
        for i in range(len(newString)):
            if newString[i] != newString[len(newString)-(i+1)]:
                return False
                exit()
        return True