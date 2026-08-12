class Solution:
    def jump(self, nums: List[int]) -> int:
        j=0
        c=0
        s=0
        for i in range(0,len(nums)-1):
            s=max(s,i+nums[i])
            if i==c:
                c=s
                j+=1
                if c==len(nums)-1:
                    return j
        return j