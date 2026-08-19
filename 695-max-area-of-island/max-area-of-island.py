class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def fun(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]==0:
                return 0
            grid[i][j]=0
            l=fun(i+1,j)
            r=fun(i-1,j)
            u=fun(i,j-1)
            d=fun(i,j+1)
            return l+u+r+d+1
        marea=0
        for i in range (len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    a=fun(i,j)
                    marea=max(marea,a)
        return marea