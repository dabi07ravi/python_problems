
num = int(input("enter the number: "))


def fibo(a, b, n):
    if n <= 0:
        return
    print(a)
    fibo(b, a+b, n-1)

fibo(0, 1, num)
