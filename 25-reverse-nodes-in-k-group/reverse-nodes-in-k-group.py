# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        ind = 1
        last = None
        prev = None
        curr = head
        first = head

        while curr:
            Next = curr.next
            curr.next = prev
            if ind % k == 0:
                if last:
                    last.next = curr
                else:
                    head = curr
                last = first
                first = Next
                curr = None

            prev = curr
            curr = Next
            ind += 1
        

        l2 = prev
        prev = None

        while l2:
            Next = l2.next
            l2.next = prev
            prev = l2
            l2 = Next

        last.next = prev

        return head