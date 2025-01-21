class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0  # Initialize the count of flowers we can place
        length = len(flowerbed)  # Length of the flowerbed array
        
        for i in range(length):  # Iterate through each spot in the flowerbed
            # Check if the current spot is empty and neighbors are valid
            if flowerbed[i] == 0:
                # Check left and right neighbors
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if left_empty and right_empty:  # If both neighbors are valid
                    flowerbed[i] = 1  # Place a flower here
                    count += 1  # Increment the count of placed flowers
                    
                    if count >= n:  # If we've placed enough flowers
                        return True  # Return True early
        
        return count >= n  # After the loop, check if we placed enough flowers
