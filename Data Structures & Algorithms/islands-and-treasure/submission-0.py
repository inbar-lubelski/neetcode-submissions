class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return None
        
        n_row= len(grid)
        n_col= len(grid[0])
        INF = 2147483647
        directions= [[1,0],[-1,0],[0,1],[0,-1]]

        def multiBfs(q):
            while q:
                r,c= q.popleft()
                for dr,dc in directions:
                    row= r+dr
                    col= c+dc
                    if row in range(n_row) and col in range(n_col) and grid[row][col] == INF:
                        grid[row][col]= grid[r][c]+1
                        q.append((row,col))





        q= collections.deque()
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j]==0:
                    q.append((i,j))

        multiBfs(q)

        


        