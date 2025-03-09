"""
1
01
101
0101
10101


hint=
1 -0
2-0,1
3-0,1,2

"""

n=int(input("enter : "))
for i in range (1,n+1):
    for j in range(i):
        print((i+j)%2,end="")
    print()    

