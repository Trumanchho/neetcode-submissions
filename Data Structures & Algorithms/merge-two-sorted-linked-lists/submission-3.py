# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head, curr, other = list1, list1, list2
        else: head, curr, other = list2, list2, list1

        while curr.next != None:
            if curr.next.val > other.val:
                tmp = curr.next
                curr.next = other
                other = tmp
            curr = curr.next
        
        curr.next = other
        
        return head

