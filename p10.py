"""
1    1
12  21
123321                          
"""
n=int(input("enter : "))
for i in range(1,n+1):
    for j in range (1,i+1):
        print(j,end="")
    print(" "*(2*(n-i)),end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print("\n")         