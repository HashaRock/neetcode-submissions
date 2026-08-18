"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodemap = {}

        def dfs(nod):
            if not nod or nod in nodemap:
                return

            newnod = Node(nod.val)
            nodemap[nod] = newnod

            for neighbor in nod.neighbors:
                dfs(neighbor)
            
            newnod.neighbors = [nodemap[neigh] for neigh in nod.neighbors]
            
        dfs(node)
        return nodemap.get(node, None)