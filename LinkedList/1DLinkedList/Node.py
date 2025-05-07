
class LinkedListNode:
    def __init__(self,data,next1=None):
        self.data = data
        self.next = next1

y = LinkedListNode(10,"abc")
print(y.data, y.next)