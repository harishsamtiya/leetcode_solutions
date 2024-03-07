# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head

        while temp:
            n += 1
            temp = temp.next

        n = (n+2)//2
        mid = 0
        temp = head 
        while temp:
            mid += 1
            if mid == n:
                return temp
            temp = temp.next
