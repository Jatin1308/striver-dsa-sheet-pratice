def oddEvenList(head) :
    l = []
    if head is None or head.next is None:
        return head
    oddTemp = head
    evenTemp = head.next
    while oddTemp is not None:
        l.append(oddTemp)
        if oddTemp.next is not None:
            oddTemp = oddTemp.next.next
        else:
            break
    while evenTemp is not None:
        l.append(evenTemp)
        if evenTemp.next is not None:
            evenTemp = evenTemp.next.next
        else:
            break
    temp = head
    for ele in l[1:]:
        temp.next = ele
        temp = temp.next
    temp.next = None
    return head


def optimalApproach(head):

    # for empty and single node LL
    if head is None or head.next is None:
        return head

    # initializing the pointers
    odd = head
    even = head.next
    evenHead = head.next

    while even is not None and even.next is not None:
        # pointing current Odd node's next to next Odd node
        odd.next = even.next
        # moving the odd to the next pointed node
        odd = odd.next

        # pointing the current even node's next to next even node
        even.next = odd.next
        # moving the even to the next pointed node
        even = even.next

    # we should point the odd to evenHead so that both gets attached and then return the initial head
    odd.next = evenHead

    return head