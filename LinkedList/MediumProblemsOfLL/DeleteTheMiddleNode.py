def deleteMiddleMoreOptimal(head):
    slow = head
    fast = head
    midPrev = None

    if not head:
        return None
    if not head.next:
        return None
    while fast and fast.next:
        fast = fast.next.next
        midPrev = slow
        slow = slow.next
    midPrev.next = slow.next

    return head

def deleteMiddleOptimal(head):
    if head is None:
        return head
    elif head.next is None:
        return None
    slow = head
    fast = head

    while fast is not None:

        if fast.next.next is None:
            slow.next = slow.next.next
            break

        elif fast.next.next.next is None:
            slow.next = slow.next.next
            break

        slow = slow.next
        fast = fast.next.next
    return head