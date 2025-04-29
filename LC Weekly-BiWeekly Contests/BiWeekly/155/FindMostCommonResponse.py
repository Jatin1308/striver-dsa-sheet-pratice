from typing import List
from collections import Counter
def findCommonResponse(self, list_of_lists: List[List[str]]) -> str:
    unique_words_across_lists = []
    for internal_list in list_of_lists:
        unique_words = list(set(internal_list))  # Remove duplicates within the inner list
        unique_words_across_lists.extend(unique_words)

    word_counts = Counter(unique_words_across_lists)

    if not word_counts:
        most_common = ""  # Handle the case of an empty input
    else:
        max_frequency = -1
        most_common = ""
        candidates = []

        for word, count in word_counts.items():
            if count > max_frequency:
                max_frequency = count
                candidates = [word]
            elif count == max_frequency:
                candidates.append(word)


        print(candidates)
        most_common = min(candidates)  # Lexicographically smallest among tied candidates

    return most_common