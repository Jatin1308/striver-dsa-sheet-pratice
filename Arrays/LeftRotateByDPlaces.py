def rotateArray(arr: list, k: int) -> list:

    if k <= 0:
        return arr

    for i in range(k):
        arr.append(arr.pop(0))

    return arr