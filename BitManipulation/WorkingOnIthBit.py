

def setIthBit(n,i):
    return n | (1<<i)
print(setIthBit(9,2))


def clearIthBit(n,i):
     return n & (~(1<<i))

print(clearIthBit(13,2))

def toggleIthBit(n,i):
    return n ^ (1<<i)
print(toggleIthBit(13,2))


def checkIfPowerOf2(n):
    if n == 0:
        return False
    if n & n - 1 == 0:
        return True
    return False
print(checkIfPowerOf2(16))