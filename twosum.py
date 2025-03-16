n=[2,7,11,15]
target=9
index_map={}

#way1
# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#        if (n[i]+n[j])==target:
#            print([i,j])

#way2
for index,value in enumerate(n):
    c=target-value
    if c in  index_map:
       print([index_map[c],index])   
    index_map[value]=index           