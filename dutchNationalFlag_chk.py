


def dutchNationalFlag(a):

    low = 0
    high = len(a)-1
    mid = 0
    temp = None

    while(mid <= high):

        if a[mid] == 0:
            temp = a[mid]
            a[mid] = a[low]
            a[low] = temp
            low = low + 1
            mid = mid +1
        elif a[mid] == 1:
            mid = mid+1
        else:
            temp = a[mid]
            a[mid]  = a[high]
            a[high] = temp
            high = high-1
    return a 




print(dutchNationalFlag([0,0,1,1,0,2,1,2,0]))