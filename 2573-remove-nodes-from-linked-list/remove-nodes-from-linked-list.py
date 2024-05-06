# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def reverseList(listHead):
            prev = None
            curr = listHead
            while curr:
                Next = curr.next
                curr.next = prev
                prev = curr 
                curr = Next
            return prev
        
        head = reverseList(head)
        maxi = 0

        prev = None
        curr = head
        while curr:
            if curr.val < maxi:
                prev.next = curr.next
            else:
                maxi = curr.val
                prev = curr
            curr = curr.next


        return reverseList(head)
