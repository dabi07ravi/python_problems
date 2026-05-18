





def countInversion(a, count):

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if i < j and a[i] > a[j]:
                count = count+1
    return count



print(countInversion([6,3,5,2,7], 0))



