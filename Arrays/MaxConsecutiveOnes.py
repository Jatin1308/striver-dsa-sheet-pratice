def traffic(n: int, m: int, vehicle: [int]) -> int:
    # m -> how many ones are flipped
    zeroCount = 0
    i = 0
    ans = 0
    for j in range(len(vehicle)):
        if vehicle[j] == 0:
            zeroCount += 1

        while zeroCount > m:
            if vehicle[i] == 0:
                zeroCount -= 1
                i += 1
        ans = max(ans, j - i + 1)
        return ans

print(traffic(5,2,[1,1,0,0,1]))
