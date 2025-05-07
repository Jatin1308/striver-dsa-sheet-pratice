"""
An anagram is a word or phrase formed by rearranging
the letters of a different word or phrase, using all
the original letters exactly once
"""

from collections import Counter
def isAnagram(s: str, t:str) -> bool:
    return Counter(s) == Counter(t)

print(isAnagram("rcar","arcr"))