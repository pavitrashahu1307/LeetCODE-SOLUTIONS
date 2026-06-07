class Solution:
    def reverse(self, x: int) -> int:
        # Step 1: Check if the number is negative
        is_negative = x < 0
        
        # Step 2: Reverse the absolute value using string slicing
        reversed_x = int(str(abs(x))[::-1])
        
        # Step 3: Reapply the negative sign if original x was negative
        if is_negative:
            reversed_x = -reversed_x
            
        # Step 4: Strict 32-bit signed integer overflow check
        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
            
        return reversed_x
