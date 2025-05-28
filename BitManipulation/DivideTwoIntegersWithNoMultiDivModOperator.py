import sys
MAX_INT_32 = 2**31 - 1
MIN_INT_32 = -2**31


def divide(dividend,divisor):

    if dividend == divisor:
        return 1
    if dividend == 0:
        return 0
    sign = True
    if dividend < 0 < divisor: sign = False
    if dividend > 0 > divisor: sign = False

    a = abs(dividend)
    b = abs(divisor)
    ans = 0

    while a>=b:
        print("Ans: ",ans)
        cnt = 0
        # while a>= (b*2**cnt+1):
        # can be written as:
        while a>=(b << cnt):
            # ans += 2**cnt
            # can be written as:
            ans += (1<<cnt)
            print("Inner Ans: ",cnt)
            a = a-(b*(1<<cnt))
            cnt += 1

    if ans > MAX_INT_32:
        return MAX_INT_32
    if ans < MIN_INT_32:
        return MIN_INT_32
    return ans if sign else -1*ans



# a/b
print(divide(22,3))
