def myPow(x,n):
    if n == 0:
        return 1.0
    if n < 0:
        return 1 / myPow(x, -n)

    if n % 2 == 0:
        half_pow = myPow(x, n // 2)
        return half_pow * half_pow
    else:
        return x * myPow(x, n - 1)

print(myPow(2.00000,-2))
