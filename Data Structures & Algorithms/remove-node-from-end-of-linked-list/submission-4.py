# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return head.next
        j = 1
        end = head
        while end.next:
            end = end.next
            j += 1
        i = j - n
        #return i
        if i == 0:
            return head.next
        cur = head
        prev = head
        while i > 0:
            prev = cur
            cur = cur.next
            i -= 1
        prev.next = cur.next

        return head