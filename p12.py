"""
A
AB
ABC
ABCD
ABCDE
"""

n=int(input("enter : "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(65+j-1),end="")
 
      
    print()    

#revrese
for i in range(n+1,0,-1):
    for j in range(1,i+1):
        print(chr(65+j-1),end="")
 
      
    print()    


    