def longestSubStrKDistinctChar(a, k):

    fmap = {}
    maxWindow = float("-inf")
    left = 0

    for right in range(len(a)):
        rightChar = a[right]

        if rightChar in fmap:
            fmap[rightChar] = fmap[rightChar] + 1
        else:
            fmap[rightChar] = 1

        while len(fmap) > k:
            leftChar = a[left]

            fmap[leftChar] = fmap[leftChar] - 1

            if fmap[leftChar] == 0:
                del fmap[leftChar]

            left = left + 1

        if len(fmap) <= k:
            windowLen = right - left + 1
            if windowLen > maxWindow:
                maxWindow = windowLen

    else:
        return maxWindow


print(longestSubStrKDistinctChar("aaabbccd", 2))
