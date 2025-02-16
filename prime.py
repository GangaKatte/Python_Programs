n=int(input("enter :"))
flag=False
if n==1:
    print("it is not prime")
elif n>1:
    for i in range (2,n):
        if(n%i==0):
            flag==True
            break    

if flag:
    print("not prime")
else:
    print("prime")     