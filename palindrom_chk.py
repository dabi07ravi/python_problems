


str = 'madam'

start = 0
end = len(str)-1

pali = True

while start < end:
    if(str[end] != str[start]):
        pali = False
        break
    start += 1
    end -= 1


print("result", pali)