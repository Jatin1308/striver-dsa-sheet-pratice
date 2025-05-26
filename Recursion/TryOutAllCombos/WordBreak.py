def wordBreak(s,l):
    d = set(l)
    def solve(start,end):
        if end == len(s):
            if s[start:end+1] in d:
                return True
            return False
        if s[start:end+1] in d:
            if solve(end+1,end+1):
                return True
        return solve(start,end+1)
    return solve(0,0)

print(wordBreak("leetcode",["leet","code"]))