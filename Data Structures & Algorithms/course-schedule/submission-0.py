class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map={i:[] for i in range( numCourses)}
        for n,pre in prerequisites:
            pre_map[n].append(pre)
        status = [0]*numCourses

        def hasCycle(node):
            if status[node]==1:
                return True
            if status[node]==2:
                return False
            
            status[node]=1
            for pre in pre_map[node]:
                if hasCycle(pre):
                    return True
            
            status[node]=2
            return False

        for n in range (numCourses):
            if status[n]==0:
                if hasCycle(n):
                    return False
        return True


        