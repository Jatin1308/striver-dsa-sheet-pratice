def expressionAddOperators(num,target):
    result = []
    num = num.lstrip('0')

    # def solve(index,num,target,curr,prev,res):
    #     print("curr: ",curr,"res: ",res)
    #     if index == len(num):
    #         if res == target:
    #             result.append(curr)
    #         return
    #     st = ""
    #     currRes = 0
    #
    #     for i in range(index,len(num)):
    #         if i > index and num[index] == '0':
    #             break
    #         st+=num[i]
    #         currRes = currRes * 10 + int(num[0])
    #         if index == 0:
    #             solve(i+1,num,target,st,currRes,currRes)
    #         else:
    #             solve(i+1,num,target,curr+"+"+st,currRes,res+currRes)
    #             solve(i + 1, num, target, curr + "-" + st, -currRes, res - currRes)
    #             solve(i + 1, num, target, curr + "*" + st, prev*currRes, res - prev + (prev*currRes))
    #
    # solve(0,num,target,"",0,0)
    # return result

    def withEval(ind,curr):
        print("Called With: "+curr)
        if ind == len(num):
            if eval(curr) == target:
                result.append(curr)
            return

        if ind == 0:
            curr+=num[ind]
            withEval(ind+1,curr)
        else:
            withEval(ind + 1, curr + "+" + num[ind])
            withEval(ind + 1, curr + "-" + num[ind])
            withEval(ind + 1, curr + "*" + num[ind])
            withEval(ind + 1, curr  + num[ind])

    withEval(0,"")
    return result
# print(expressionAddOperators("00000132",6))
print(expressionAddOperators("105",5))