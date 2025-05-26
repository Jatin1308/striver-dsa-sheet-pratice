def binaryToDecimal(b):
    res = 0
    b = b[::-1]
    for i in range(len(b)):
        res+=int(b[i])*(2**i)
    return res
print("Binary to decimal of 1101: ",binaryToDecimal('1101'))


def decimalToBinary(decimal):
    b = ""
    while decimal != 0:
        b+=str(decimal%2)
        decimal = decimal//2
    return b
print("Decimal to binary of 13: ",decimalToBinary(13))