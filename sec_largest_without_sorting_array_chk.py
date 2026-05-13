


def secLargest(a):
    temp = None
    firstMax = float('-inf')
    secMax = float('-inf')
    for i in range(a):
        if a[i] > firstMax:
            temp = firstMax
            secMax = temp
            firstMax = a[i]
    else:
        print(firstMax,secMax)

secLargest([1,2,6,90,3,5])