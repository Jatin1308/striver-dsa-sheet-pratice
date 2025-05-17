
def atoi(s) -> int:
    INT_MIN = -2 ** 31
    INT_MAX = 2 ** 31 - 1

    def sanitize(inputS):
        d = dict.fromkeys(map(str, range(10)), 0)
        isNegative = False
        toRet = ""
        sanitizedString = inputS.strip()
        if len(sanitizedString) == 0:
            return True, toRet
        if sanitizedString[0] == "-":
            isNegative = True
            sanitizedString = sanitizedString[1:]
        elif sanitizedString[0] == "+":
            sanitizedString = sanitizedString[1:]

        print("Sanitized:", sanitizedString)

        for i, ele in enumerate(sanitizedString):
            if ele in d:
                toRet += ele
            else:
                break
        return isNegative, toRet

    def solve(inputS):
        if len(inputS) == 1:
            return int(inputS)
        last = inputS[-1]
        rest = inputS[:-1]
        last = int(last)
        return solve(rest) * 10 + last

    isNeg, x = sanitize(s)
    if len(x) == 0:
        return 0
    res = solve(x)
    if isNeg:
        res = -1 * res

    if res < INT_MIN:
        return INT_MIN
    elif res > INT_MAX:
        return INT_MAX
    else:
        return res

print(atoi("-91283472332"))