class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=0
        r=len(h)-1
        marea=0
        while l<r:
            breadth=(r-l)
            if h[l]<=h[r]:
                height=h[l]
                l+=1
            else:
                height=h[r]
                r-=1
            area=height*breadth
            marea=max(marea,area)
        return marea