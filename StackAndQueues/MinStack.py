class MinStack:
    # we will store pair(int,int) -> pair(valueAppended, minTillNow)

    def __init__(self):
        self.stack = []
        self.min = 2 ** 31
        self.length = 0

    def pop(self) -> None:

        if self.length > 0:
            poppedEle = self.stack.pop()
            # print("Popped: ",poppedEle)
            self.length -= 1

    def top(self) -> int:
        # print("stack for TOP: ",self.stack)
        if self.length > 0:
            return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

    def push(self, val: int) -> None:
        if self.length == 0:
            self.min = val
            self.stack.append((val, val))
        else:
            self.stack.append((val, min(val, self.getMin())))
        self.length += 1
        # print("Append: ",self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()