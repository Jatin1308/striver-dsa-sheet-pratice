"""
input -> tree
output -> eetr or eert, 'e' is occurring twice so need to come first and then the less occurring char
"""

def frequencySort(s) -> str:
    from collections import Counter
    from collections import OrderedDict
    sd = Counter(s)
    '''
    res = ""
    # Sort the items (key-value pairs) of the Counter based on the value
    sorted_items = sorted(sd.items(), key=lambda item: item[1], reverse=True)
    print(sorted_items)
    # Create a new ordered dictionary from the sorted items
    sorted_sd = OrderedDict(sorted_items)

    for k,v in sorted_sd.items():
        res+=(k*v)
    return res
    '''

    return "".join(k*v for k,v in sd.most_common())


print(frequencySort("tree"))
# print(frequencySort("cccaaa"))