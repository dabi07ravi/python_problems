


def reverseStr(str):
    # lst = list(str)
    # lst.reverse()
    # return ''.join(lst)
    i =0
    lst = list(str)
    j = len(lst)-1
    while i < j:
        temp = lst[j]
        lst[j] = lst[i]
        lst[i] = temp
        i += 1
        j -= 1
    return ''.join(lst)

print(reverseStr('Hello'))