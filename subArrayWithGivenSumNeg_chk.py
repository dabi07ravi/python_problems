

def subArrayWithGivenSumNegative(a, t):

    
    currentSum = 0
    subArray = []
    map = {}
    map[0] = -1

    for i in range(len(a)):
        currentSum = currentSum + a[i]

        need = currentSum - t

        if need in map:
            index = map[need]
            subArray.append(a[index+1:i+1])
        
        map[currentSum] = i

    return subArray

print(subArrayWithGivenSumNegative([3,4,7,2,-3,1,4,2], 7))