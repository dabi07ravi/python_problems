def mergeInterval(a):

    a.sort()

    start = a[0][0]
    end = a[0][1]
    c = []

    for i in range(1, len(a)):
        s = a[i][0]
        e = a[i][1]

        if s <= end:
            end = max(end,e)
        else:
            c.append([start, end])
            start = s
            end = e

    c.append([start,end])
    return c




print(mergeInterval([[1,3],[2,6],[8,10],[15,18], [13,20]]))