"""
E
DE
CDE
BCDE
ABCDE

"""
n=int(input("enter :"))
for i in range(n):
    for j in range(i+1):
        print(chr(ord('E')-i+j),end="")
        
    print()