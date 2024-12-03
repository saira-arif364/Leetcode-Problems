# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
        # First solution
        # if len(s) != len(t):
        #     return False
        # counter = {}
        # for char in s:
        #     counter[char]= counter.get(char,0) + 1
        # for char in t:
        #     if char not in counter or counter[char]==0:
        #         return False
        #         counter[char] -=1
        # return True
        # Second solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        
        # Count the frequency of characters in string s
        for x in s:
            count[x] += 1
        
        # Decrement the frequency of characters in string t
        for x in t:
            count[x] -= 1
        
        # Check if any character has non-zero frequency
        for val in count.values():
            if val != 0:
                return False
        
        return True

        