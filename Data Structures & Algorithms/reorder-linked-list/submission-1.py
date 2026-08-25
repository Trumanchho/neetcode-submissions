# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # hmap = {}
        # i = 0
        # tmp = head
        # while tmp != None:
        #     hmap[i] = tmp
        #     tmp = tmp.next
        #     i += 1

        hmap = []
        tmp = head
        while tmp != None:
            hmap.append(tmp)
            tmp = tmp.next

        dummy = ListNode()
        left = 0
        right = len(hmap)-1

        while left<=right:
            print(left)
            print(right)
            dummy.next = hmap[left]
            dummy = dummy.next
            if left != right:
                dummy.next = hmap[right]
                dummy = dummy.next
            left+= 1
            right-=1
        dummy.next = None

