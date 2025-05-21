"""
find subset of length k which makes sum n
and each number will be used once
"""
def combinationSum3(reqLengthOfSubs,whatIsTheSum):
    arr = range(1,10)
    res = []

    def solve(ind,n,sub):
        # print("solve called with ind: ",ind, "subs: ",sub,"res: ",res)
        if len(sub) == reqLengthOfSubs:
            # print("Length matched,sub: ",sub)
            if n == 0:
                res.append(list(sub))
            return
        if n == 0:
            if len(sub) == reqLengthOfSubs:
                res.append(list(sub))
            return
        if ind >= len(arr):
            print("Index greater: ",ind)
            if n == 0:
                res.append(list(sub))
            return
        sub.append(arr[ind])
        solve(ind+1,n-arr[ind],sub)
        sub.pop()
        solve(ind+1,n,sub)
    solve(0, whatIsTheSum, [])
    return res


# print(combinationSum3(3,7))
# print(combinationSum3(3,9))



def morOptimal(reqLengthOfSubs, whatIsTheSum):
    res = []

    def solve(ind, current_sum, current_combination):
        # Pruning 1: If current_sum exceeds whatIsTheSum or current_combination
        # is already too long, no need to proceed with this path.
        # This is crucial for early exits.
        if current_sum > whatIsTheSum:
            return
        if len(current_combination) > reqLengthOfSubs:
            return

        # Base Case 1: A valid combination is found
        if current_sum == whatIsTheSum and len(current_combination) == reqLengthOfSubs:
            res.append(list(current_combination))
            return

        # Pruning 2: If we've exhausted all possible numbers (1-9)
        # and haven't found a valid combination, return.
        if ind > 9:  # Since numbers are from 1 to 9 (inclusive)
            return

        # Pruning 3: If the remaining numbers are not enough to reach reqLengthOfSubs
        # or if the smallest possible sum from remaining numbers + current sum
        # exceeds whatIsTheSum, we can prune.
        # (9 - ind + 1) is the number of remaining elements including current 'ind'
        remaining_elements = 9 - ind + 1
        if reqLengthOfSubs - len(current_combination) > remaining_elements:
            return

        # Pruning 4: Smallest possible sum from remaining elements
        # If current_sum + sum of remaining smallest numbers is still less than whatIsTheSum
        # but we can't add any more numbers (already at reqLengthOfSubs), then this path is invalid.
        # This is more complex and often handled implicitly by other prunings,
        # but can be added for extra strictness.
        # For simplicity, let's focus on the more direct prunings first.

        # Recursive Step 1: Include the current number (arr[ind] which is 'ind')
        # Only include if adding 'ind' doesn't exceed the target sum
        # And if we haven't already reached the required length of the combination
        if current_sum + ind <= whatIsTheSum and len(current_combination) < reqLengthOfSubs:
            current_combination.append(ind)
            solve(ind + 1, current_sum + ind, current_combination)
            current_combination.pop()  # Backtrack

        # Recursive Step 2: Exclude the current number (arr[ind] which is 'ind')
        # Only proceed if there are still numbers to consider (ind < 9)
        solve(ind + 1, current_sum, current_combination)

    # Start the recursion from number 1 (ind=1)
    solve(1, 0, [])
    return res


print(morOptimal(3,9))