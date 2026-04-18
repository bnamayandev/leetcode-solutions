# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        dummy1 = head

        while dummy1.next:
            length += 1
            dummy1 = dummy1.next
        
        nodeIndex = length - n

        if nodeIndex == 0 :
            return head.next

        dummy2 = head

        for i in range(nodeIndex - 1):
            dummy2 = dummy2.next
            print(dummy2.val)
        
        if dummy2 and dummy2.next:
            dummy2.next = dummy2.next.next
        
        else:
            return None

        return head