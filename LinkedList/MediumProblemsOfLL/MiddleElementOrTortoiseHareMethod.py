def middleOfLinkedList(head):
    slow = head
    fast = head

    while slow is not None and fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow