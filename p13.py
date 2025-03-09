"""
A
BB
CCC
DDDD
"""
n=int(input("enter:"))
for i in range(1,n+1):
    print(chr(64+i)*i,end="")
    print()    
