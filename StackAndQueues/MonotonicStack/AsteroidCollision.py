
def asteroidCollision(arr):
    arr = asteroids
    stack = []

    for ele in arr:
        if ele > 0:
            stack.append(ele)
        else:
            if stack and stack[-1] > abs(ele):
                continue
            else:
                while stack and 0 < stack[-1] < abs(ele):
                    stack.pop()
                if stack and stack[-1] == abs(ele):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(ele)

    return stack


print(asteroidCollision([5,10,-5]))
print(asteroidCollision([10,2,-5]))
print(asteroidCollision([8,-8]))
