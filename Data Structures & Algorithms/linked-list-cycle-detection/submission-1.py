# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next:
            slow = head
            fast = head.next
            while (fast != slow) and (fast != None):
                slow = slow.next
                if fast.next:
                    fast = fast.next
                if fast.next:
                    fast = fast.next
            if fast.next != None:
                return True
        return False