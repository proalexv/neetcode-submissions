class Solution:
    def isPalindrome(self, s: str) -> bool:
        # trivial solution 
        # arraryString = [c.lower() for c in s if c.isalnum()]
        # return arraryString == arraryString[::-1]

        # two pointer solution

        L, R = 0, (len(s) - 1)
        
        while L < R: 
            while L < R and not (s[L].isalnum()): 
                L += 1 
            while  L < R and not (s[R].isalnum()):
                R -= 1
            if s[L].lower() != s[R].lower():
                return False
            L += 1
            R -= 1
        return True