class Solution:
    def trap(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        rb=h[r]
        lb=h[l]
        w=0
        while l<r:
            if lb<=rb:
                l+=1
                lb=max(lb,h[l])
                w=w+(lb-h[l])
            else:
                r-=1
                rb=max(rb,h[r])
                w=w+(rb-h[r])
        return w
