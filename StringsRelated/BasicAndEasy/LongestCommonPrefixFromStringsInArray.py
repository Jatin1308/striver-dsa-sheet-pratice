def getPrefix(l):
    l = sorted(l)


    first = l[0]
    last = l[-1]
    ans = ""
    i,j = len(first),len(last)
    c1,c2 = 0,0

    while c1<i and c2 < j:
        if (first[c1] != last[c2]) and c1==0 and c2==0:
            return ""
        if first[c1] == last[c2]:
            ans+=first[c1]
            c1+=1
            c2+=1
        else:
            return ans
    return ans

print(getPrefix(["flower","flow","flight","flat"]))
print(getPrefix(["abc","def","ghi"]))