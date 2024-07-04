# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head.next
        prev =  head
        summ = 0
        
        while curr:
            if curr.val == 0:
                if summ != 0:
                    curr.val = summ
                    summ = 0
                    prev.next = curr
                    prev = curr
            else:
                summ += curr.val
            
            curr = curr.next
        
        head = head.next
            
        return head