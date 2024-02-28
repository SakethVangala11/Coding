# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res= []
        q = [root]
        lefty = root
        while q:
            qlen = len(q)
            lefty = q[0]
            for i in range(qlen):
                node = q.pop(0)
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        print(res)

        return lefty.val



        