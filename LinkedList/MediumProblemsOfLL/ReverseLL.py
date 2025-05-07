def reverseList( head ):
    if head is None:
        return

    temp = head
    prev = None
    # temp.next = prev
    while temp is not None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front
    return prev