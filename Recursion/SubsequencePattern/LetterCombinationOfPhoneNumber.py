def letterCombOfPhoneNumber(digits):
    digToChar = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = []
    if len(digits) == 0:
        return res
    def solve(indOfDigits, currString):

        if len(currString) == len(digits):
            res.append(currString)
            return

        for c in digToChar[digits[indOfDigits]]:
            solve(indOfDigits+1,currString+c)
    solve(0,"")
    return res

print(letterCombOfPhoneNumber("23"))