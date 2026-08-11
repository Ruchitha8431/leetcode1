class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={0:-1}
        sum=0
        for i in range(0,len(nums)):
            sum+=nums[i]
            rem=sum%k
            if rem in d:
                if i-d[rem]>=2:
                    return True
            else:
                     d[rem]=i
        return False