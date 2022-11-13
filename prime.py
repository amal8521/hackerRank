# n = int(input("number"))
from cmath import sqrt


n = 4
flag = 0 
if(n > 1):   
    for i in range(2, n):
        if n % i == 0:
            flag = 1      # factor is found so not prime
            break
    if(flag):
     print(n,"is not prime")
    else:
        print(n,"is prime")
else:
    print("number greater than 1 is required")