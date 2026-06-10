class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to use the two-pointer technique
        nums.sort()
        
        # Initialize closest_sum with the sum of the first three elements
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums) - 2):
            # Two-pointer initialization
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If we find an exact match to the target, return it immediately
                if current_sum == target:
                    return current_sum
                
                # If the current sum is closer to the target than our previous closest_sum, update it
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on how current_sum compares to the target
                if current_sum < target:
                    left += 1   # We need a larger sum, move left pointer right
                else:
                    right -= 1  # We need a smaller sum, move right pointer left
                    
        return closest_sum
