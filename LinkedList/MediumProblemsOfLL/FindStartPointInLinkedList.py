from errno import ELOOP


def detectCycle(head):
    if head is None or head.next is None:
        return None
    slow = head
    fast = head

    while slow is not None and fast is not None:
        slow = slow.next
        fast = fast.next
        if fast is None:
            return None
        fast = fast.next

        # once we know have a loop, we will reset the slow or fast pointer
        # to head and then move one by one
        if fast == slow:
            # print("Detected a loop")
            slow = head
            pos = 0

            while True:
                if slow == fast:
                    return slow
                slow = slow.next
                fast = fast.next
                # print("Inside 2nd step/while")
                pos += 1
    return None


# to find the length of loop after second step, let the slow pointer be there and start another loop
# for one pointer slow/fast one by one to come to slow again and count number of steps