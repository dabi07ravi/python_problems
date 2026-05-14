
import math


def squareRoot(num):

    low = 0
    high = num
    ans = None

    while(low <= high):
        mid = math.floor((low+high)/2)

        if mid*mid == num:
            return mid
        elif mid * mid < num:
            ans  = mid
            low = mid+1
        else:
            high = mid-1
    
    return ans
         


   
    

print(squareRoot(63))