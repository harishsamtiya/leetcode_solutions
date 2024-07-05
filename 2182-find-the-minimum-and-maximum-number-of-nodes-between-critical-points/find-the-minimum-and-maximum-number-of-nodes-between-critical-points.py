# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [10**5, -1]
        firstCriticalPos = None
        prevCriticalPos = None

        pos = 1

        temp = head.next
        prev = head
        while temp.next:
            if  (prev.val < temp.val  and temp.next.val < temp.val) or (prev.val > temp.val  and temp.next.val > temp.val):
                prevCriticalPos = pos
                firstCriticalPos = pos
                break
            pos += 1
            prev = temp
            temp = temp.next


        prev = temp
        temp = temp.next
        pos += 1
        if temp:
            while temp.next:
                if  (prev.val < temp.val  and temp.next.val < temp.val) or (prev.val > temp.val  and temp.next.val > temp.val):
                    result[0] = min(result[0], pos - prevCriticalPos)
                    prevCriticalPos = pos
                pos += 1
                prev = temp
                temp = temp.next
        
        if result[0] == 10**5:
            result[0] = -1

        if firstCriticalPos and firstCriticalPos != prevCriticalPos:
            result[1] = prevCriticalPos - firstCriticalPos
        return result