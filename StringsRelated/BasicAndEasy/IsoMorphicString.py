from collections import Counter

def isomorphicString(s,t):
    if len(s)!= len(t):
        return False

    d={}
    for i in range(len(s)):
        original = s[i]
        replacement = t[i]

        if original not in d:
            if replacement not in d.values():
                d[original] = replacement
            else:
                return False
        else:
            if d[original] != replacement:
                return False
    return True




print(isomorphicString("egg","add"))
# isomorphicString("foo","bar")