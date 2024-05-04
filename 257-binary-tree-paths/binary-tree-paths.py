# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        final_paths = []
        path = ""
        def dfs(root, path):
            if not root.left and not root.right:
                path+=str(root.val)
                final_paths.append(path)
                return 
            if root.left:
                dfs(root.left, path + str(root.val) + "->" )
            if root.right:
                dfs(root.right, path  + str(root.val) + "->" )

        dfs(root, path)
        return final_paths
                
        