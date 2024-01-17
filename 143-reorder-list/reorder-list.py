# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        n = 0
        curr = head
        while curr: 
            n += 1
            curr = curr.next

        if n <= 2:
            return head

        curr = head
        for i in range(n//2):
            curr = curr.next
        temp = curr
        l2 = curr.next
        temp.next = None

        prev = l2
        curr = l2.next
        while curr:
            temp = curr
            curr = curr.next
            prev.next = curr

            temp.next = l2
            l2 = temp


        curr = head
        while l2:
            temp = l2
            l2 = l2.next

            temp.next = curr.next
            curr.next = temp
            curr = temp.next
        return head


        