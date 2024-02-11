# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=[]
        x=head
        while(x):
            l.append(x.val)
            x = x.next
        l[k-1],l[len(l)-k]= l[len(l)-k],l[k-1]
        head = ListNode(l[0])
        currHead = head
        for i in range(1,len(l)):
            currHead.next  = ListNode(l[i])
            currHead = currHead.next
        return head


 
        


        
        
            
        





        