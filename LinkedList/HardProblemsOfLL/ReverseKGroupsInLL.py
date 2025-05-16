from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def findKthNode(head, k):
            k -= 1
            while head is not None and k > 0:
                k -= 1
                head = head.next
            return head

        def reverseLL(head):
            if head is None:
                return
            temp = head
            prev = None
            while temp is not None:
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
            return prev

        temp = head
        nextNode = ListNode(-1)
        prevNode = None
        while temp is not None:
            knode = findKthNode(temp, k)
            print("Found kth Node: ", knode)
            if knode is None:
                print("Knode is None")
                if prevNode:
                    prevNode.next = temp
                break
            nextNode = knode.next
            knode.next = None
            reverseLL(temp)

            if temp == head:
                print("first group")
                head = knode
            else:
                prevNode.next = knode
            prevNode = temp
            temp = nextNode
        return head


