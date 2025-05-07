def longestPalindromicSubstring(s):
    lengthOfString = len(s)
    if lengthOfString <=1:
        return s

    result = ""

    for i in range(1,lengthOfString):

    # consider odd length string
        low = i
        high = i

        while s[low] == s[high]:
            low-=1
            high+=1

            if low == -1 or high == lengthOfString:
                break

        palindrome = s[low+1:high]
        print("i: ",i,"Odd palindrome: "+palindrome)
        if len(palindrome) > len(result):
            result = palindrome

    # consider even length string
        low = i-1
        high = i

        while s[low] == s[high]:
            low-=1
            high+=1

            if low==-1 or high == lengthOfString:
                break
        palindrome = s[low+1:high]
        print("i: ",i,"Even palindrome: " + palindrome)
        if len(palindrome) > len(result):
            result = palindrome

    print("Result: ",result)
    return result






# print(longestPalindromicSubstring("abrbadaadab"))
print(longestPalindromicSubstring("babad"))