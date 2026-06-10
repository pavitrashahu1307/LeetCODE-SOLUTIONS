class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Edge case: if needle is empty, the problem typically defines the output as 0
        if not needle:
            return 0
            
        h_len = len(haystack)
        n_len = len(needle)
        
        # Loop through the haystack, but stop where needle can no longer fit
        for i in range(h_len - n_len + 1):
            # Check if the slice matches the needle
            if haystack[i:i + n_len] == needle:
                return i
                
        # If no match is found after checking all positions
        return -1
