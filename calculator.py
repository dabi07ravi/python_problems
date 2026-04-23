
num1 = float(input("enter num one: "))
num2 = float(input("enter num two: "))


action = input('enter the action: ' ).lower()


if action == 'add':
    print(f"sum of two num : {num1+num2}")
elif action == 'sub':
    print(f"subtract of two num : {num1-num2}")
elif action == 'div':
    print(f"division of two num : {num1/num2}")
elif action == 'mul':
    print(f"multiplication of two num : {num1*num2}")
else:
    print("invalid action")


