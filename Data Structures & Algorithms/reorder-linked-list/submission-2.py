# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        nodeList = []
        tmp = head
        while tmp != None:
            nodeList.append(tmp)
            tmp = tmp.next

        dummy = ListNode()
        left = 0
        right = len(nodeList)-1

        while left<=right:
            print(left)
            print(right)
            dummy.next = nodeList[left]
            dummy = dummy.next
            if left != right:
                dummy.next = nodeList[right]
                dummy = dummy.next
            left+= 1
            right-=1
        dummy.next = None

