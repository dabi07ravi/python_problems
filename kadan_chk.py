def kadan(a):

    currentSum = 0
    subArray = []
    maxSum = float("-inf")
    endIndex = 0
    startIndex = 0
    tempStart = 0

    for i in range(len(a)):
        currentSum = currentSum + a[i]

        if currentSum > maxSum:
            maxSum = currentSum

            startIndex = tempStart
            endIndex = i

        if currentSum <= 0:
            currentSum = 0
            tempStart = i + 1

    subArray = a[startIndex : endIndex + 1]
    return subArray, maxSum


print(kadan([2, 1, -3, 4, -1, 2, 1, -5, 4]))
