from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # To adjacency list
        def to_adjacency(numCourses,  prerequisites):
            ajc = { i:[] for i in range(numCourses)}
            for child, parent in prerequisites:
                ajc[child].append(parent)
            return ajc
        
        # dfs (with recursive)
        def dfs_helper(start):
            # Base case 1 - Return False if found in visted, means have loop
            if start in visited : return False
            # Base case 2 - Return True if is empty, means this course no dependency of others
            elif not ajc[start] : return True  
            visited.add(start)
            
            for parent in ajc[start]:
                # if any course not completed, final result will be False
                if not dfs_helper(parent): 
                    return False
            visited.remove(start)
            ajc[start] = []
            return True 
        
        ajc = to_adjacency(numCourses, prerequisites)
        #print("ajc:", ajc)
        visited = set()
        for start in range(numCourses):
            if not dfs_helper(start):
                print(False)
                return False
        print(True)
        return True

slt = Solution()
cases = [
    (5, [[1,4],[2,4],[3,1],[3,2]]),
    (2,[[1,0]]),
    (4, [[1,0], [0,2],[2,3],[3,1],[2,0]]),
    (20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]])
]
# Test Case
for numCourses, prerequisites in cases:
    slt.canFinish(numCourses, prerequisites)

"""
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that 
you must take course bi first if you want to take course ai.

For example, 
the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: true
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0. So it is possible.

Example 2:
    Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
    Output: false
    Explanation: There are a total of 2 courses to take. 
    To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
    
Constraints:
    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.

"""