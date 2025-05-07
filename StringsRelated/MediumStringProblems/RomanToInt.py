def romanToInt(s:str):
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = d[s[len(s)-1]]
    print(total)
    i = len(s) - 2

    while i > -1:
        print(i,s[i],d[s[i]])
        if d[s[i]] < d[s[i+1]]:
            total-=d[s[i]]
        else:
            total+=d[s[i]]
        i-=1

    return total

# romanToInt("III")
# romanToInt("IV")
# romanToInt("LVIII")
romanToInt("MCMXCIV")
