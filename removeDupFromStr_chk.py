

def removeDup(str):
    result = ''
    for i in range(len(str)):
        duplicate = False
        for j in range(i):
            if(str[i] == str[j]):
                duplicate = True
                break

        if not duplicate:
            result = result + str[i]
    else:
        return result

print(removeDup('programming'))