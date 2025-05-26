def checkIfIthBitIsSetOrNot(n,i):
    """
        brute -> convert the number to binary
                 check the ith bit of the binary
        we can use left shift and "&" operator
        if n & (1 << i) != 0-> then bit is set otherwise bit is not set

        or right shift
        if (n >> i) & 1 == 1 then set else not set
    """

    if n & (1 << i) != 0:
        return True
    # return False
     
    if (n >> i) & 1 == 1:
        return True
    return False

print(checkIfIthBitIsSetOrNot(0,2))