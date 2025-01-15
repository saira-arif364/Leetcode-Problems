class Solution:
    def romanToInt(self, s: str) -> int:
        # Map Roman numerals to their integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0  # To keep track of the previous numeral's value

        # Traverse the string in reverse order
        for char in reversed(s):
            current_value = roman_to_int[char]
            
            if current_value < prev_value:
                # If current value is smaller, subtract it
                total -= current_value
            else:
                # Otherwise, add it
                total += current_value
            
            # Update the previous value
            prev_value = current_value
        
        return total
