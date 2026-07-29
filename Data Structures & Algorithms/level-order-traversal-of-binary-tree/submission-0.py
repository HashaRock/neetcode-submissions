# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            qlen = len(queue)
            lvl = []
            for i in range(qlen):
                nod = queue.popleft()
                if nod:
                    lvl.append(nod.val)
                    queue.append(nod.left)
                    queue.append(nod.right)
            if lvl:
                res.append(lvl)
        
        return res