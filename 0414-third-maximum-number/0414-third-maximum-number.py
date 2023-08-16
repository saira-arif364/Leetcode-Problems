class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=set(nums)
        if len(s)<3:
            return max(s)
        elif len(s)==3:
            return min(s)
        else:
            s.remove(max(s))
            s.remove(max(s))
            return max(s)