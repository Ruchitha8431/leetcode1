class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        pro=1
        for i in nums:
            l.append(pro)
            pro=pro*i
        r=1
        for i in range(len(nums)-1,-1,-1):
            l[i]=l[i]*r
            r=r*nums[i]
        return l