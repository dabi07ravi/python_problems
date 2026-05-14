import math


a = [1, 2, 3, 4, 5, 6, 7]
target = 2


def binarySearchRec(a, t, low, high):
    mid = math.floor((low+high)/2)
    if a[mid] == t:
        return mid
    elif a[mid] > t:
        return binarySearchRec(a, t, low, mid-1)
    else:
        return binarySearchRec(a, t, mid+1, high)

print(binarySearchRec(a, target, 0, len(a)-1))
