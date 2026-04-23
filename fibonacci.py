# num = int(input("enter the number: "))
# ls = [0,1]

# def fibonacci(n):
#     for i in range(2, n+1):
#         ls.append((ls[-1] + ls[-2]))
#     else:
#         print("listtt", ls)


# fibonacci(num)


a = 0
b = 1
print(a)
print(b)
for i in range(2, 6):
    c = a + b
    print(c)
    a = b
    b = c
    