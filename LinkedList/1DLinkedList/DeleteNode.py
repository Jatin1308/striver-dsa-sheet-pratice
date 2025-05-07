"""
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second
node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
"""
from .Node import LinkedListNode


def deleteNode(node: LinkedListNode):

    # node passed is node to be deleted
    node.data = node.next.data
    node.next = node.next.next
