num = int(input("enter the number: "))


def fact_chk(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact_chk(n-1)
print(fact_chk(num))