

def remove_outermost_parentheses(s):
    count = 0
    ans = ""
    for c in s:
        if c == ')':
            count-=1
        if count != 0 :
            ans+=c
        if c == '(':
            count+=1
        print("Answer: ",ans)



    print(ans)
    return ans

