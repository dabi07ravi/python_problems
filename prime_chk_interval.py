
lower = int(input("enter the lower number"))

higher = int(input("enter the higher number"))


for num in range(lower, higher+1 ):
    if( num > 1 ):
        for i in range(2, num):
            if(num % i == 0):
                break
        else:
            print("prime number: ", num)
        