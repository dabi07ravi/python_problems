

def findAllAnagram(a, t):


    fmap = {}
    left = 0
    req = len(t)
    index = []

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

        while( right-left + 1 == len(t)):
            if req == 0:
                index.append(left)
            leftChar = a[left]
            
            if leftChar in fmap:
                fmap[leftChar] = fmap[leftChar] + 1

                if fmap[leftChar] > 0:
                    req = req + 1
            left = left+1
    else:
        return index
   



print(findAllAnagram('cbaebabacd', 'abc'))