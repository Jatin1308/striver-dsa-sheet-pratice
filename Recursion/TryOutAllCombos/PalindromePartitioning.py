def palindromicPartitioning(s):
    res = []
    part = []
    def checkPal(inp):
        return inp == inp[::-1]
    def solve(i):
        if i == len(s):
            res.append(part.copy())
        for j in range(i,len(s)):
            if checkPal(s[i:j+1]):
                part.append(s[i:j+1])
                solve(j+1)
                part.pop()
    solve(0)
    return res
print(palindromicPartitioning("aab"))