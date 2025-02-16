n=int(input("enter the num:"))
sum_powers=0
temp=n
l=len(str(n))

while temp > 0:
    sum_powers +=(temp%10)**l
    temp //= 10
    
    
if (sum_powers == n):
        print("Armstrong")
else:
        print("Not armstrong")    
