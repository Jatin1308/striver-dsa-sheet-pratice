def bruteSolFindInterSection(headA, headB):
    """ brute force sol """
    d = {}
    tempA = headA
    tempB = headB
    while tempA is not None:
        d[tempA] = 1
        tempA = tempA.next

    while tempB is not None:
        if tempB in d:
            return tempB
        tempB = tempB.next
    return None

def optimal(headA,headB):
    """optimal sol"""
    al = 0
    bl = 0
    tempA = headA
    tempB = headB
    if headA == headB:
        return headB

    while tempA is not None:
        al += 1
        tempA = tempA.next
    while tempB is not None:
        bl += 1
        tempB = tempB.next
    tempA = headA
    tempB = headB

    if al < bl:
        for i in range(bl - al):
            tempB = tempB.next
    elif bl < al:
        for i in range(al - bl):
            tempA = tempA.next

    while tempA is not None:
        if tempA == tempB:
            return tempA
        tempA = tempA.next
        tempB = tempB.next
    return None
