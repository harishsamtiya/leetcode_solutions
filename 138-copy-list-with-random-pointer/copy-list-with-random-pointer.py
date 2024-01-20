"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new_head = Node(head.val)

        hashmap = dict()
        hashmap[head] = new_head

        node = head.next
        prev = new_head
        while node:
            new_node = Node(node.val)
            prev.next = new_node
            hashmap[node] = new_node
            prev = new_node
            node = node.next
        
        node = head
        new_node = new_head

        while node:
            if node.random :
                new_node.random = hashmap[node.random]
            else:
                new_node.random = None

            new_node = new_node.next
            node = node.next


        return new_head