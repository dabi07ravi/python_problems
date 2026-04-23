


def chkAnagram(a, b):
    #  through reverse method
    # lsta = list(a)
    # lstb = list(b)

    # lsta.sort()
    # lstb.sort()

    # if(lsta == lstb):
    #     return True
    # else:
    #     return False

    if len(a) != len(b):
        return False

    map = {}

    for ch in a:
        count = 1
        if ch in map:
            map[ch] = count + 1
        else:
            map[ch] = count
   

    for ch in b:
        count = 1
        if ch in map:
            map[ch] = count - 1
            if map.get(ch) == 0:
                del map[ch]
        else:
            map[ch] = count
    

    if len(map) == 0:
        return True
    else:
        return False


        


print(chkAnagram('listen', 'silent'))