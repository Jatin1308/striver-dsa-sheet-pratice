from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        curr = dummy
        t1 = l1
        t2 = l2
        carry = 0
        s = 0
        while t1 is not None or t2 is not None:
            s = carry
            if t1:
                s += t1.val
            if t2:
                s += t2.val
            newNode = ListNode(s % 10)
            carry = s // 10
            curr.next = newNode
            curr = curr.next

            if t1:
                t1 = t1.next
            if t2:
                t2 = t2.next
        if carry != 0:
            newNode = ListNode(carry)
            curr.next = newNode
        return dummy.next
