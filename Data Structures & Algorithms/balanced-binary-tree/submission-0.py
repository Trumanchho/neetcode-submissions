# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return (True, 0)
            l_isBal, l_h = dfs(root.left)
            r_isBal, r_h = dfs(root.right)
            return ((abs(l_h - r_h) <= 1) and (l_isBal and r_isBal), max(l_h, r_h)+1)

        return dfs(root)[0]
