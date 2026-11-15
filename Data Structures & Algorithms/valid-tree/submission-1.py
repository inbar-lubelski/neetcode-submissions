class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return n==1
        
        if len(edges)!= n-1:
            return False

        visited= set()
        neigbors= {i:[] for i in range(n)}
        for i,ne in edges:
            neigbors[i].append(ne)
            neigbors[ne].append(i)

        def dfs(node,prev):
            if node in visited:
                return False
            visited.add(node)

            for ne in neigbors[node]:
                if ne==prev:
                    continue
                if not dfs(ne,node):
                    return False
            return True

        return dfs(0,-1) and len(visited)==n

        
        