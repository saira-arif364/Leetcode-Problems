class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return True  # An empty or single-element array is monotonic by default.
        
        increasing = decreasing = True  # Initialize flags for both conditions.

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                decreasing = False  # If current is greater, it can't be decreasing.
            elif nums[i] < nums[i - 1]:
                increasing = False  # If current is smaller, it can't be increasing.
            
            # If neither increasing nor decreasing, exit early.
            if not increasing and not decreasing:
                return False

        return True  # If we complete the loop, it's monotonic.
        