nums=[1,2,3,4]

n=len(nums)
output=[1]*n
left_product=1
right_product=1

for i in range(n):
    output[i]=left_product #here we are saying that what ever left product comes that will be store in output of i
    left_product*=nums[i]
    print(left_product)

for i in range(n-1,-1,-1):
    output[i]*=right_product # here we are multplying current output of i x right side output
    right_product*=nums[i]
    print(right_product)


print(output)


        