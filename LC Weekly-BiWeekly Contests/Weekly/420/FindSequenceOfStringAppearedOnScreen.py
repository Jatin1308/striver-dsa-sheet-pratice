from typing import List
def stringSequence(target: str) -> List[str]:

    result  = []

    current = ""

    for char in target:
         # press key1 to append 'a' to the current string

         current+='a'

         result.append(current)

         while current[-1] != char:
              current = current[:-1]+ chr((ord(current[-1]) - ord('a')+1)%26 + ord('a'))
              result.append(current)

    return result


print(stringSequence("abc"))

print(stringSequence('he'))