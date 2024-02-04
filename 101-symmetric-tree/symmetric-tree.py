# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(lTree,rTree):
            if not lTree and not rTree:
                return True
            elif not lTree or not rTree:
                return False
            return ((lTree.val == rTree.val) and dfs(lTree.left,rTree.right) and dfs(lTree.right,rTree.left))
        return dfs(root.left,root.right)
        
        