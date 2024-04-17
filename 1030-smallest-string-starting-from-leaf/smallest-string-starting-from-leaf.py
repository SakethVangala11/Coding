# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        s = []
        def dfs(root, temp):
            if not root.left and not root.right:
                temp+=chr(root.val+97)
                s.append(''.join(temp[::-1]))
                return 
            if root.left:
                dfs(root.left, temp + chr(root.val+97))
            if root.right:
                dfs(root.right, temp + chr(root.val+97))
        dfs(root, "")
        s.sort()
        return s[0]       