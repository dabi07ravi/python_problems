


def mergeSortedArray(a, b):
    c = []
    i  = 0
    j = 0

    while(i < len(a) and j < len(b)):

        if a[i] < b[j]:
            c.append(a[i])

            i = i+1
        else:
            c.append(b[j])

            j = j+1


    while(i < len(a)):
         c.append(a[i])
         i = i+1

    while(j < len(b)):
        c.append(b[j])
        j = j+1


    return c




print(mergeSortedArray([1,3,5,7], [2,4,6,8, 11, 12]))