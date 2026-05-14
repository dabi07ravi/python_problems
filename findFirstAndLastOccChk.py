

import math


def findFirstOccu(a, t):
    low = 0
    high = len(a) -1
    ans = None
    while low <= high:
        mid = math.floor((low+high)/2)
        if a[mid] == t:
            ans = mid
            high = mid -1
        elif a[mid] > t:
            high = mid - 1
        else:
            low = mid + 1
    return ans

def findLastOccu(a, t):
    low = 0
    high = len(a) -1
    ans = None
    while low <= high:
        mid = math.floor((low+high)/2)
        if a[mid] == t:
            ans = mid
            low = mid + 1
        elif a[mid] > t:
            high = mid - 1
        else:
            low = mid + 1
    return ans


print(findFirstOccu([1, 2, 3, 3, 3, 6, 7], 3), findLastOccu([1, 2, 3, 3, 3, 6, 7], 3)),