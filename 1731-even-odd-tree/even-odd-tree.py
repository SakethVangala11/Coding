# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = [root]
        level = 0
        while q:
            qlen = len(q)
            print(level)
            if level%2==0:
                prev = -1
            else:
                prev = 9999999
            for i in range(qlen):
                node = q.pop(0)
                if level%2==0:
                    if node.val%2==0:
                        return False
                    else:
                        if node.val <= prev:
                            return False
                        else:
                            prev = node.val
                else:
                    if node.val%2!=0:
                        return False
                    else:
                        if node.val>=prev:
                            return False
                        else:
                            prev = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return True
        