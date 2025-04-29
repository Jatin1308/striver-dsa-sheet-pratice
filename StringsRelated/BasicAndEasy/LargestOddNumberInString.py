def findLargestOddSubstring(s):

    frontCounter = 0

    for i in range(len(s)-1,-1,-1):
        if int(s[i])%2!=0:
            return s[:i+1]
        else:
            continue
    else:
        return ""

print("Ans: ",findLargestOddSubstring("8888877772"))
print("Ans: ",findLargestOddSubstring("8888888"))
print("Ans: ",findLargestOddSubstring("52"))
print("Ans: ",findLargestOddSubstring("21"))


# more efficient:

def efficient(s):
    for i in range(len(s)-1,-1,-1):
        if s[i] in {'1','3','5','7','9'}:
            return s[:i+1]
    return ""

