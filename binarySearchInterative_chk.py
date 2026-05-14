import math

def binarySearch(a, t):

    low = 0
    high = len(a)-1

    while low <= high:

        mid = math.floor((low+high)/2)

        if a[mid] == t:
            return mid
        elif a[mid] > t:
            high = mid-1
        else:
            low = mid + 1

print(binarySearch([1, 2, 3, 4, 5, 6, 7], 2))
