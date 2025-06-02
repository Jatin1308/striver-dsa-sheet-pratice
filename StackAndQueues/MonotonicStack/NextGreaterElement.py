from typing import List
def nextGreaterElement(a: List[int], b: List[int]) -> List[int]:
    ans = []
    for ele in a:
        print("Checking Element: {} and ans till now: {}".format(ele,ans))
        for i in range(len(b)):
            if ele == b[i]:
                for j in range(i+1,len(b)):
                    print("Comparing ele: {} and b[j]: {}".format(ele,b[j]))
                    if b[j]>ele:
                        ans.append(b[j])
                        break
                else:
                    ans.append(-1)
    print(ans)
    return ans




# # print(nextGreaterElement([4,1,2],[1,3,4,2]))
# print(nextGreaterElement([2,4],[1,2,3,4]))

def ansWithMonotonicStack(a,b):
    stack = []
    nge = [-1]*len(b)
    for i in range(len(b)-1,-1,-1):

        while stack and b[i] > stack[-1]:
            stack.pop()

        if stack:
            nge[i] = stack[-1]
        stack.append(b[i])

    res = []
    for n in a:
        for j in range(len(b)):
            if n == b[j]:
                res.append(nge[j])
                break
    return res


print(ansWithMonotonicStack([4,1,2],[1,3,4,2]))
print(ansWithMonotonicStack([2,4],[1,2,3,4]))