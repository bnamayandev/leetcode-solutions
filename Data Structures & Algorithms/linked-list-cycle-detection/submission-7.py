# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        
        s, f = head, head.next

        while f:
            if s == f:
                return True
            s = s.next
            if f.next:
                f = f.next.next
            else:
                return False


        return False
        