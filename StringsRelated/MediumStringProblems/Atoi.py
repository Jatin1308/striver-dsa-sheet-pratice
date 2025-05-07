def myAtoi( s: str) -> int:
    d = dict.fromkeys(map(str, range(10)),0)
    # print("Dict: ",d)

    isNeg = False
    op = ""
    for ele in s:
        if ele == '-':
            if len(op) != 0:
                break
            isNeg = True
        elif ele == '+':
            if len(op) != 0:
                break

        elif ele in d:
            op+=ele
        elif ele == " " or ele == "+":
            continue
        else:
            break

    if len(op) == 0 or (isNeg and op == ""):
        return 0

    result = int(op) * -1 if isNeg else int(op)

    # Clamp the result to the 32-bit signed integer range
    min_32bit = -2 ** 31
    max_32bit = 2 ** 31 - 1
    if result < min_32bit:
        return min_32bit
    elif result > max_32bit:
        return max_32bit
    else:
        return result
# print(myAtoi("1337c0d3"))
# print(myAtoi("  -042"))
# print(myAtoi("0-1"))
# print(myAtoi("words and 987"))


# def myAtoi(s: str) -> int:
#     s = s.strip()  # Remove leading/trailing spaces
#     if not s:
#         return 0
#
#     sign, i, res = 1, 0, 0
#
#     # Check for sign
#     if s[0] == '-':
#         sign = -1
#         i += 1
#     elif s[0] == '+':
#         i += 1
#
#     while i < len(s) and s[i].isdigit():
#         res = res * 10 + int(s[i])
#
#         # Handle overflow
#         if sign * res > 2 ** 31 - 1:
#             return 2 ** 31 - 1
#         if sign * res < -2 ** 31:
#             return -2 ** 31
#
#         i += 1
#
#     return sign * res

print(myAtoi("+-12"))