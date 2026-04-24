

def minWindowSubStr(a, t):


    fmap = {}
    left = 0
    minWindow = float('inf')
    req = len(t)
    substr = []

    for i in range(len(t)):
        ch = t[i]
        if ch in fmap:
            fmap[ch] = fmap[ch] + 1
        else:
            fmap[ch] = 1


    for right in range(len(a)):
        rightChar = a[right]

        if rightChar in fmap:
            if fmap[rightChar] > 0:
                req-=1
            fmap[rightChar] = fmap[rightChar] - 1

        while(req == 0):
            leftChar = a[left]

            windowSize = right-left+1
            if(windowSize < minWindow):
                minWindow = windowSize
                substr = a[left:right+1]
            
            if leftChar in fmap:
                fmap[leftChar] = fmap[leftChar] + 1

                if fmap[leftChar] > 0:
                    req = req + 1
            left = left+1
    else:
        return substr, minWindow
   



print(minWindowSubStr('ADOBECODEBANC', 'ABC'))