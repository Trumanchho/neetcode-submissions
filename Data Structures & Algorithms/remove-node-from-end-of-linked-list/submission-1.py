# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # sz = 0
        # tmp = head
        # while tmp:
        #   sz += 1
        #   tmp = tmp.next 
        
        # prev_i = sz-n-1
        
        # if prev_i < 0:
        #     return head.next
        
        # prev = head 
        # for i in range(prev_i):
        #     prev = prev.next
        
        # prev.next = prev.next.next

        # return head
        dummy = ListNode()
        dummy.next = head
        first, second = head, dummy
        i = 0
        while first:
            first = first.next
            i += 1
            if i > n:
                second = second.next
        
        second.next = second.next.next

        return dummy.next

