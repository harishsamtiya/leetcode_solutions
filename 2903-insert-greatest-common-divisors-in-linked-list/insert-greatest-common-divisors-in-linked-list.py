# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head.next:
            return head

        def findGCD(num1, num2):
            while num1:
                num1, num2 = num2%num1, num1
            return num2
        
        curr = head.next
        prev = head

        while curr:
            gcd = findGCD(min(prev.val, curr.val), max(prev.val, curr.val))

            newNode = ListNode(gcd, curr)

            prev.next = newNode
            prev = curr
            curr = curr.next
        
        return head