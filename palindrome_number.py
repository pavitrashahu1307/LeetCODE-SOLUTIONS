class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes (e.g., -121 reads as 121- from right)
        # Numbers ending in 0 (except 0 itself) cannot be palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_num = 0
        original = x
        
        # Reverse the integer mathematically
        while x > 0:
            last_digit = x % 10
            reversed_num = (reversed_num * 10) + last_digit
            x //= 10  # Integer division to remove the last digit
            
        return original == reversed_num
