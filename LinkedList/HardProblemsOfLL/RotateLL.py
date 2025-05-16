from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def findNthNode(head, k):
            c = 1
            while head is not None:
                if c == k:
                    return head
                c += 1
                head = head.next
            return head

        if not head or not head.next:
            return head
        l = 1
        tail = head
        while tail.next is not None:
            l += 1
            tail = tail.next
            if tail is None:
                break
        if k % l == 0:
            return head

        k = k % l
        tail.next = head
        newLastNode = findNthNode(head, l - k)
        head = newLastNode.next
        newLastNode.next = None
        return head

