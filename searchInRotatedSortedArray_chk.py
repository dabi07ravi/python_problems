
import math


def searchInRotatedArray(a, t):

    low = 0
    high = len(a)-1

    while (low < high):

        mid  = math.floor((low+high)/2)

        if a[mid] > a[0]:
            low = mid+1
        else:
            high = mid  

    pivot = low 


    if t >= a[low] and t <= a[len(a)-1]:

        low = pivot
        high = len(a)-1
    else:
        low = 0
        high = pivot-1
    

    while low <= high:
        mid = math.floor((low+high)/2)

        if a[mid] == t:
            return mid
        elif a[mid] > t:
            high = mid-1
        else:
            low = mid + 1
    







print(searchInRotatedArray([10, 11, 12, 1, 2, 3, 4], 2))