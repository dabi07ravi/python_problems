

def longestRepChar(a, k):
    fmap = {}
    left = 0
    maxFreq = 0
    maxWindow = float('-inf')

    for right in range(len(a)):
        rightChar = a[right]
        if rightChar in fmap:
            fmap[rightChar] = fmap.get(rightChar) + 1
        else:
            fmap[rightChar] = 1
        maxFreq = max(max, fmap.get(rightChar))
        windowSize = right - left + 1
        charNeedToBeChanged = maxFreq - windowSize

        if( charNeedToBeChanged > k):
            leftChar = a[left]
            if leftChar in fmap:
               fmap[leftChar] = fmap.get(leftChar) - 1 
            else:
                fmap[leftChar] = 1
            left = left + 1

        if windowSize > maxWindow:
            maxWindow = windowSize
     
        
    else:
        return maxWindow



print(longestRepChar('AABABCC', 2))