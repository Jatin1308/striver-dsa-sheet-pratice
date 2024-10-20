'''def numberOfSubstrings(s: str, k: int) -> int:
    n = len(s)

    count = 0

    # iterate over each starting point of the substring

    for i in range(n):
        freq = [0]*26


        # extend the substring from starting point i to the end
        for j in range(i,n):
            freq[ord(s[j]) - ord('a')] +=1  # update freq of current character

            if any(f>=k for f in freq):
                count+=1
    return count
'''









# TLE
'''
def numberOfSubstrings(s,k):
    n = len(s)
    count = 0

    for start in range(n):
        freq = {}

        for end in range(start,n):
            char = s[end]
            freq[char] = freq.get(char,0)+1

            if any(f >= k for f in freq.values()):
                count+=1
    return count


# sliding window approach - not working
'''

'''
def numberOfSubstrings(s: str, k: int) -> int:
    n = len(s)
    totalCount = 0

    for uniqueChars in range(1,27):

        freq = [0]*26   # freq Array from 'a' to 'z'
        left = 0
        windowUnique = 0
        charsAtLeastK = 0

        # sliding window over the string
        for right in range(n):

            # Expand the window by including s[right]
            if freq[ord(s[right]) - ord('a')] == 0:
                windowUnique+=1
            
            freq[ord(s[right])-ord('a')] +=1
            if freq[ord(s[right]) - ord('a')] == k:
                charsAtLeastK+=1


                # contract the window
                while windowUnique > uniqueChars:
                    if freq[ord(s[left]) - ord('a')] == k:
                        charsAtLeastK-=1
                    freq[ord(s[left]) - ord('a')] -=1
                    if freq[ord(s[left]) - ord('a')] == 0:
                        windowUnique -= 1
                    left+=1

                if charsAtLeastK > 0:
                    totalCount+=right-left+1

    return totalCount
'''

def numberOfSubstrings(s: str, k: int) -> int:
    n = len(s)
    total_count = 0

    # Use a frequency array for 26 lowercase letters
    freq = [0] * 26
    
    # Iterate through all possible starting points for substrings
    for start in range(n):
        # Reset frequency array for new start
        freq = [0] * 26
        count_at_least_k = 0
        
        # Expand the end pointer
        for end in range(start, n):
            # Update frequency of the current character
            char_index = ord(s[end]) - ord('a')
            freq[char_index] += 1
            
            # If the character count reaches k, increase the valid count
            if freq[char_index] == k:
                count_at_least_k += 1
            
            # If there's at least one character with count >= k,
            # count all substrings from start to end as valid.
            if count_at_least_k > 0:
                total_count += 1

    return total_count

# Test the function with the provided test case


print(numberOfSubstrings("abacb",2))


# print(numberOfSubstrings("abcde",1))

