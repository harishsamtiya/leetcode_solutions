# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l_len = 0

        curr = head
        while curr:
            l_len += 1
            curr = curr.next

        prev = None
        curr = head

        for i in range(l_len - n):
            prev = curr
            curr = curr.next
        

        if prev:
            prev.next = curr.next
        else:
            head = curr.next
        return head
        


        