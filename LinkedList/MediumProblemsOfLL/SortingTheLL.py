# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMiddle(head):
    fast = head.next   # did this because in even length LL, i want the first middle not the second one(case in MergeSort)
    slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

def mergeLL(left,right):
    newNode = ListNode(-1)
    temp = newNode

    while left is not None and right is not None:
        if left.val < right.val:
            temp.next = left
            temp = left
            left = left.next
        else:
            temp.next = right
            temp = right
            right = right.next
    if left:
        temp.next = left
    else:
        temp.next = right
    return newNode.next
def sortLL(head):
    if not head or not head.next:
        return head
    tempForMiddle = head
    middle = findMiddle(tempForMiddle)
    leftHead = head
    rightHead = middle.next
    middle.next = None
    leftHead = sortLL(leftHead)
    rightHead = sortLL(rightHead)
    return mergeLL(leftHead,rightHead)




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        def findMiddle(head):
            fast = head.next  # did this because in even length LL, i want the first middle not the second one(case in MergeSort)
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        def mergeLL(left, right):
            dummyNode = ListNode(-1)
            temp = dummyNode

            while left is not None and right is not None:
                if left.val < right.val:
                    temp.next = left
                    temp = left
                    left = left.next
                else:
                    temp.next = right
                    temp = right
                    right = right.next
            if left:
                temp.next = left
            else:
                temp.next = right
            return dummyNode.next

        if not head or not head.next:
            return head
        tempForMiddle = head
        middle = findMiddle(tempForMiddle)
        leftHead = head
        rightHead = middle.next
        middle.next = None
        leftHead = self.sortList(leftHead)
        rightHead = self.sortList(rightHead)
        return mergeLL(leftHead, rightHead)




