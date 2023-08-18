class Solution:
    def countSegments(self, s: str) -> int:
        s=s.split()
        return len(s)
        # count=0
        # for i in range(len(s)):
        #     if s[i] !='' and (i==0 or s[i-1]==''):
        #         count +=1
        #         return count        