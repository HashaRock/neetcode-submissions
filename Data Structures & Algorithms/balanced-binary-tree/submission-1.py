class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    
        def dfs(root):
            if not root:
                return [True, 0]
            l, r = dfs(root.left), dfs(root.right)
            balanced = l[0] and r[0] and abs(l[1] - r[1]) <= 1
            return [balanced, 1 + max(l[1], r[1])]
        
        return dfs(root)[0]