#Given an integer,n , perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range 2 of  to 5, print Not Weird
#If n is even and in the inclusive range 6 of  to 20, print Weird
#If n is even and greater than 20, print Not Weird
# 1 <= n <= 100

n = int(input())
if n % 2 == 1:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
