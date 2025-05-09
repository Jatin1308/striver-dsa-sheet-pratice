def detectCycle(head):

    # we can use tortoise - hare algo to check it
    slow = head
    fast = head

    while slow is not None and fast is not None:
        slow = slow.next
        fast = fast.next
        if fast is not None:
            fast = fast.next
        else:
            return False

        if slow == fast:
            return True
    return False

    # this needs extra space
    """temp = head
    d = {}
    while temp is not None:
        # print(d)
        if temp not in d:
            d[temp] = 1
        else:
            return True
        temp = temp.next
    return False"""

detectCycle("head")