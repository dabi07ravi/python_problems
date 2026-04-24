


def longestSubStr(a):

    mset = set()
    left = 0
    maxWindow = float('-inf')

    for right in range(len(a)):
        rightChar = a[right]

        while(rightChar in mset):
            leftChar = a[left]
            mset.remove(leftChar)
            left = left+1

        mset.add(rightChar)
        maxWindow = max(right-left+1, maxWindow)
    else:
        return maxWindow

print(longestSubStr("abcabcbb"))
