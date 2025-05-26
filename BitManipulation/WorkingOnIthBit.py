

def setIthBit(n,i):
    return n | (1<<i)
print(setIthBit(9,2))


def clearIthBit(n,i):
     return n & (~(1<<i))

print(clearIthBit(13,2))

def toggleIthBit(n,i):
    return n ^ (1<<i)
print(toggleIthBit(13,2))