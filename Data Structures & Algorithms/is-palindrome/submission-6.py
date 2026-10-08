class Solution:
    def isPalindrome(self, s: str) -> bool:
        # trivial solution 
        arraryString = [c.lower() for c in s if c.isalnum()]
        return arraryString == arraryString[::-1]