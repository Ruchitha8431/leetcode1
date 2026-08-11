class Solution:
    def shipWithinDays(self, w: List[int], days: int) -> int:
        def check(cap):
            day=1
            sum=0
            for i in w:
                sum+=i
                if sum>cap:
                    day+=1
                    sum=i
            return day<=days
        l=max(w)
        r=sum(w)
        ans=0
        while (l<=r):
            mid=(l+r)//2
            if check(mid):
                r=mid-1
                ans=mid
            else:
                l=mid+1
        return ans