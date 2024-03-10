"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = []
        temp = head

        while temp or stack:
            if not temp.next and stack:
                node = stack.pop()
                node.prev = temp
                temp.next = node
            
            if temp.child:
                if temp.next:
                    stack.append(temp.next)
                temp.next = temp.child
                temp.child.prev = temp
                temp.child = None

            temp = temp.next
        return head