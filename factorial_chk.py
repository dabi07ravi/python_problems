num = int(input("enter the number"))
fact = 1

if num == 1:
    print(f"factorial of {num} is {fact}")
else: 
    for i in range (2, num+1):
        fact = fact * i
    else:
        print(f"factorial of {num} is {fact}")