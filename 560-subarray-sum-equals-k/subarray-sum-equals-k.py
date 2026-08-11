class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
         d={0:1}
         sum=0
         c=0
         for i in nums:
             sum+=i
             left=sum-k
             if left in d:
                c+=d[left]
             if sum in d:
                d[sum]+=1
             else:
                d[sum]=1
         return c  