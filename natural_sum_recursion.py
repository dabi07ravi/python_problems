

num = int(input("enter the number: "))

def sumNatural(sum, n):
    if(n == 0):
        return sum
    sum = sum+ n
    return sumNatural(sum, n-1)



print(sumNatural(0, num))