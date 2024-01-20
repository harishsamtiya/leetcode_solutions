# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        summ = l1.val + l2.val
        head = ListNode(summ%10)
        carry = summ//10

        l1_node = l1.next
        l2_node = l2.next

        prev = head
        while carry or (l1_node and l2_node):
            summ = carry
            if l1_node:
                summ += l1_node.val
                l1_node = l1_node.next
            if l2_node:
                summ += l2_node.val
                l2_node = l2_node.next

            node = ListNode(summ%10)
            carry = summ//10

            prev.next = node
            prev = node
            
            
        
        if l1_node:
            prev.next = l1_node

        if l2_node:
            prev.next = l2_node
        
        return head
