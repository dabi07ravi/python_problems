

def subArrayWithGivenSum(a, t):

    left = 0
    right = 0
    sum = 0
    subArray = []

    while(right < len(a)):


        while(sum > t):
            sum = sum - a[left]
            left = left+1

        sum = sum + a[right]
        if sum == t:
            subArray = a[left:right+1]
        right = right+1

    return subArray




print(subArrayWithGivenSum([1, 10, 4, 0, 3, 5], 7))