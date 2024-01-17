# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        curr = head
        Next = head.next 

        while Next:
            curr.next = Next.next
            Next.next = head
            head = Next
            Next = curr.next
        return head