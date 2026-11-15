class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0

        if not grid or not grid[0]:
            return max_area

        range_row= len(grid)
        range_col= len(grid[0])
        visited = set()
        directions= [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(r,c):
            if (r,c) in visited or r<0 or r>=range_row or c<0 or c>=range_col or grid[r][c]==0:
                return 0 
            visited.add((r,c))
            return 1+ dfs(r+1,c) + dfs(r-1,c)+dfs(r,c+1)+dfs(r,c-1)




        for i in range(range_row):
            for j in range(range_col):
                if (i,j) not in visited and grid[i][j]==1:
                    
                    max_area= max(max_area, dfs(i,j))

        return max_area

        