from collections import Counter, defaultdict
#
#
# def beautyOfString(s):
#     if len(s)<2:
#         return 0
#
#     d = Counter(s)
#     beauty = d.most_common()[0][1] - d.most_common()[-1][1]
#     print("Received: ", s,", returning: ",beauty)
#     return beauty
#
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
# def sumOfBeautyOfAllSubstrings(s):
#     res = 0
#     for i in range(0,len(s)):
#         for j in range(i+1,len(s)+1):
#             res+=beautyOfString(s[i:j])
#     return res
# #
# # print(sumOfBeautyOfAllSubstrings("aabcb"))
# print(sumOfBeautyOfAllSubstrings("aabcbaa"))
#
# # print(sumOfBeautyOfAllSubstrings("uxojuymtfntwkqkodtkiiqvijkjfibznrxysxuiizjqxqhcnqtejhzforrjtrepsrwezsvbpdmvykhfxvwoxokiyxdrynjydmzpjpbvtrpgsgajqfcevtxevhyialvzujetbwdiminelaluqshhalfcwdcjshfqqxkjasnvcpiburffbgeajzxqfineeartacrbzdbajzgigyigvgxwjherilmobjbjguofhieymxoxygwqbuehywe"))



def moreConcise(s):

    res = 0

    for i in range(len(s)):
        maxF = float("-inf")
        freq = defaultdict(int)
        for j in range(i,len(s)):
            freq[s[j]]+=1
            print(freq)
            maxF = max(maxF,freq[s[j]])
            res+= maxF-min(freq.values())
    return res

print(moreConcise("aabcbaa"))