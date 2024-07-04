# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head.next
        left =  head
        summ = 0
        
        while curr:
            if curr.val == 0:
                left = left.next
                left.val = summ
                summ = 0
            else:
                summ += curr.val
            
            curr = curr.next
        left.next = None
        return head.next