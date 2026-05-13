


def rotateArray(elm):

    for k in range(2):

        rightElm = elm[len(elm)-1]
        for i in reversed(range(len(elm))):

            elm[i] = elm[i-1]
        else:
            elm[0] = rightElm

    return elm

    for k in range(2):

        leftElement = elm[0]

        for i in range(len(elm)-1):
            elm[i] = elm[i+1]
        else:
            elm[len(elm)-1] = leftElement
    
    return elm

print(rotateArray([1,2,3,4,5]))