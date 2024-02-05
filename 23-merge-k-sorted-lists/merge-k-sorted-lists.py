# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def merge(list1, list2):
            if list1.val > list2.val:
                list1, list2 = list2, list1
            
            head = list1

            prev= list1
            curr = list1.next

            while curr and list2:
                if prev.val <= list2.val <= curr.val:
                    temp = list2
                    list2 = list2.next

                    prev.next = temp
                    temp.next = curr
                    curr = temp

                else:
                    prev = curr
                    curr = curr.next
            
            if list2:
                prev.next = list2
            
            return head
        
        def merge_lists(lists):
            if lists:
                l1 = None
                while lists and not l1:
                    l1 = lists.pop()
                
                if not l1:
                    return None

                l2 = None
                while lists and not l2:
                    l2 = lists.pop()
                
                if not l2:
                    return l1
                
                l1 = merge(l1, l2)
                l2 = merge_lists(lists)

                if not l2:
                    return l1
                return merge(l1, l2)
                
            return None

        return merge_lists(lists)


                
