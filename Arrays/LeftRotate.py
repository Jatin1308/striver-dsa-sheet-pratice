from sys import *
from collections import *
from math import *


def rotateArray(arr: [], n: int) -> []:
    arr.append(arr.pop(0))
    return arr

rotateArray([1,2,3,4],4)