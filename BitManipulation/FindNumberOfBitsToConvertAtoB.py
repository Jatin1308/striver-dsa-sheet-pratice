def findNumberOfBits(start,goal):
    """
        XOR works on different bits
        same bits -> 0
        different bits -> 1
    """

    # this will give res where 1 is set where it needs to be flipped
    res = start^goal
    cnt = 0
    for i in range(31):
        if res & (1<<i):
            cnt+=1
    return cnt



print(findNumberOfBits(10,7))