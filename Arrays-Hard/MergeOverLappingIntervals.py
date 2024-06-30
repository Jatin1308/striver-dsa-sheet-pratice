def merge(intervals):

    intervals = sorted(intervals)
    ans = []
    for i in range(len(intervals)):
        if len(ans) == 0 or intervals[i][0] > ans[-1][1]:
            ans.append(intervals[i])
        else:
            ans[-1][1] = max(ans[-1][1],intervals[i][1])
    return ans


    '''
    # nlogn complexity
    intervals = sorted(intervals)
    ans = []
    for i in range(len(intervals)):
        start = intervals[i][0]
        end = intervals[i][1]

        if len(ans)!=0 and end <= ans[-1][1]:
            continue
        
        for j in range(i,len(intervals)):
            if intervals[j][0] <= end:
                end = max(end, intervals[j][1])
            else:
                break
        ans.append([start,end])

    return ans
'''





    # fixPointer = 0
    # next = fixPointer+1
    # ans = []
    # while fixPointer < len(intervals):
    #     print(ans, fixPointer,next)
    #     if next < len(intervals):
    #         if intervals[fixPointer][1] >= intervals[next][0]:
    #             start = intervals[next][0] if intervals[next][0]  < intervals[fixPointer][0] else intervals[fixPointer][0]
    #             end = intervals[next][1] if intervals[next][1]  > intervals[fixPointer][1] else intervals[fixPointer][1]
    #             ans.append([start,end])
    #             next+=1
    #         else:
    #             fixPointer = next
    #     else:
    #         return ans
            

# print("Final Ans: ",merge([[1,3],[2,6],[8,10],[15,18]]))
print("Final Ans: ",merge([[1,4],[4,5]]))
# print("Final Ans: ",merge([[1,4],[0,4]]))

        



