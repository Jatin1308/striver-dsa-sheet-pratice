def reverseWords(s):
    # to put the words in the correct order like:
    # input: "Hello world" -> "dleow olleh" -> no i will pick each word reverse it and then add to answer
    s = s[::-1]
    def sanitizeString(inputString):
        op = ""
        currentWord = ""
        l = len(inputString)
        i = 0
        while i<l:
            # fetching the single word out of string
            while i<l and inputString[i]!=" ":
                currentWord+=inputString[i]
                i+=1
            # adding the fetched string to answer after reversing
            if len(currentWord) > 0:
                # need this check to add single space between words of the string
                if len(op)>0:
                    op+=" "
                op+=currentWord[::-1]
                currentWord = ""
            i+=1
        return op
    print("ans:",sanitizeString(s))
reverseWords("the pen")


def revOptimized(s):
    words = s.split()  # Splits the string into a list of words
    reversed_words = [word for word in words[::-1]]  # Reverses each word
    return " ".join(reversed_words)
print("*"+revOptimized("   the pen  ")+"*")