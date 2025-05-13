from ReverseLL import reverseList
def isLinkedListPalindrome(head):
    """
        1. put all the elements in the stack
        2. again iterate on LL, compare each element with top of the stack
            if all elements are equal then LL is palindromic
    """

    l = []
    temp = head
    while temp is not None:
        l.append(temp.val)
        temp = temp.next
    temp = head

    for ele in l[::-1]:
        if ele != temp.val:
            return False
        temp = temp.next
    else:
        return True

isLinkedListPalindrome(123)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    we do not want to use the extra space
"""

def withoutExtraSpace(head):
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    reversedLLHead = reverseList(slow)

    first = head
    second = reversedLLHead

    while second is not None:
        if first.val != second.val:
            reverseList(reversedLLHead)
            return False
        first = first.next
        second = second.next
    reverseList(reversedLLHead)
    return True




