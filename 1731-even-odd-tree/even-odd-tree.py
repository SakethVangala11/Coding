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
            result = []
            for i in range(qlen):
                node = q.pop(0)
                result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level%2==0:
                for i in range(len(result)-1):
                    if result[i]%2==0 or result[i+1]<=result[i]:
                        return False
                if result[-1]%2==0:
                    return False
            else:
                for i in range(len(result)-1):
                    if result[i]%2!=0 or result[i+1]>=result[i]:
                        return False
                if result[-1]%2!=0:
                    return False
            print(result)
            level+=1
        return True
        