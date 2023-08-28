class Solution:
    def countVowels(self, word: str) -> int:
        sum=0
        length=len(word)
        dic={'a':1,'e':1,'i':1,'o':1,'u':1}
        for i in range(length):
            if word[i] in dic:
                sum +=(length-i)*(i+1)
                
        return sum
            