class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')  # Fixed the set syntax
        s = list(s)  # Convert string to a list for mutability
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]  # Swap vowels
                left += 1
                right -= 1
            if s[left] not in vowels:  # Move left pointer if not a vowel
                left += 1
            if s[right] not in vowels:  # Move right pointer if not a vowel
                right -= 1
                
        return "".join(s)  # Join the list back into a string
