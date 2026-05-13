




def chkArraySorted(elm):

    ascSorted = True
    descSorted = True

    for i in range(len(elm)-1):

        if elm[i] < elm[i+1]:
            descSorted = False
        

        if elm[i] > elm[i+1]:
            ascSorted = False

    
    return ascSorted or descSorted






   

print(chkArraySorted([1,3,5,7,35, 45]))