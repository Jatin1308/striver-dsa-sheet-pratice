def generateSubsequences(l):
    res = []
    n = len(l)
    subs = []

    def solve(ind,subs):
        if ind >= n:
            print(subs)
            res.append(list(subs))
            return

        # take the current index element and add in current subsequence we are working on
        subs.append(l[ind])
        solve(ind+1,subs)

        # we need to remove it so that we can create the subsequence without taking the current ele as well
        subs.pop()
        solve(ind+1,subs)
    solve(0,subs)
    return res


print(generateSubsequences([1,2,3]))