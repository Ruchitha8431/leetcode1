class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        h=1
        l=1
        ph=1
        pl=1
        m=max(nums)
        for i in nums:
            h=ph*i
            l=pl*i
            ph=max(h,l,i)
            pl=min(h,l,i)
            if ph>m:
                m=ph
        return m
