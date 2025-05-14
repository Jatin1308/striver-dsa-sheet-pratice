def removeNthNodeFromBack(head,n):
    # bruteforce approach
    temp = head
    if head is None:
        return head
    elif head.next is None and n == 1:
        return None
    else:
        length = 0
        while temp is not None:
            length += 1
            temp = temp.next
        temp = head
        count = length - n
        if length == n:
            head = head.next
            return head
        while temp is not None:
            count -= 1
            if count == 0:
                break
            temp = temp.next
        # delNode = temp.next
        temp.next = temp.next.next
        return head



def optimalApproach(head,n):
    slow = head
    fast = head

    if head is None:
        return head
    elif head.next is None and n == 1:
        return None
    else:
        while fast is not None and n != 0:
            n -= 1
            fast = fast.next
        if fast is None:
            head = head.next
            return head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head