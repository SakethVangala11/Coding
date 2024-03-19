# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        min_val = float('inf')
        second_min_val = float('inf')
        q = [root]
        while(q):
            qlen = len(q)
            node = q.pop(0)
            if node.val<min_val:
                second_min_val = min_val
                min_val = node.val
            elif node.val < second_min_val and node.val!=min_val:
                second_min_val = node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if second_min_val!=float('inf'):
            return second_min_val
        return -1
            



        