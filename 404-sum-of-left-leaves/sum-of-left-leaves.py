# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sumo = 0
        q = deque([(root, False)])
        while q:
            qlen = len(q)
            for i in range(qlen):
                node, position = q.popleft()
                if node.left:
                    q.append((node.left,True))
                if node.right:
                    q.append((node.right, False))
                if position and not node.left and not node.right:
                    sumo+=node.val
        return sumo


        