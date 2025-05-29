def checkValidWithStack(s):
    openB = ('(', '{', '[')
    closed = (')','}',']')
    stack = []
    for bracket in s:
        if bracket in openB:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            if (bracket == closed[0] and stack[-1] == openB[0]) or (bracket == closed[1] and stack[-1] == openB[1]) or (bracket == closed[2] and stack[-1] == openB[2]):
                stack.pop()
            else:
                return False
    if len(stack)!=0:
        return False
    return True


# print(checkValidWithStack("()[]{}"))
print(checkValidWithStack("(]"))


