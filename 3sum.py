class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sorting makes it easy to skip duplicates and use two pointers
        
        for i in range(len(nums)):
            # If the current number is greater than 0, the remaining numbers 
            # will also be greater than 0, so no three numbers can sum to 0.
            if nums[i] > 0:
                break
                
            # Skip duplicate values for the first element to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Two-pointer setup
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum > 0:
                    right -= 1  # Sum is too large, move the right pointer left
                elif three_sum < 0:
                    left += 1   # Sum is too small, move the left pointer right
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # Skip duplicate values for the right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return res
